from flask import Flask, render_template, request
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

app = Flask(__name__)

metrics = GunicornInternalPrometheusMetrics(app)
metrics.info('app_info', 'Frontend Service', version='1.0')

app = Flask(__name__)


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )
    return config.initialize_tracer()


@app.route("/")
def homepage():
    with tracer.start_span('home-span') as span:
        span.set_tag('home-tag', 'Sample from home')
        return render_template("main.html")


tracer = init_tracer('frontend-service')
tracing = FlaskTracing(tracer, True, app)


if __name__ == "__main__":
    app.run()
