import logging
from flask import Flask, jsonify, render_template
from flask_opentracing import FlaskTracing
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_flask_exporter import PrometheusMetrics

from flask_pymongo import PyMongo


app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application info", version="1.0")

JAEGER_HOST = getenv("JAEGER_HOST", "localhost")
logging.getLogger("").handlers = []
logging.basicConfig(format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def init_tracer(service):

    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
            "local_agent": {"reporting_host": JAEGER_HOST},
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()


tracer = init_tracer("backend-service")

flask_tracer = FlaskTracing(tracer, True, app)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config["MONGO_URI"] = (
    "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"
)

mongo = PyMongo(app)


@app.route("/")
def homepage():
    with tracer.start_span('home-span') as span:
        span.set_tag('home-tag', 'Sample from home')
        return "Hello World"


@app.route("/api")
def my_api():
    with tracer.start_span('api-span') as span:
        span.set_tag('api-tag', 'Sample from api')
        answer = "something"
        return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
