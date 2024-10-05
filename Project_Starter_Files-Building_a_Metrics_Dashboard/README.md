**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
![image](https://github.com/user-attachments/assets/c3d1b964-4d83-4209-884e-1cca5714a230)

![Screenshot 2024-10-01 222239](https://github.com/user-attachments/assets/b7263369-5cfe-4bcb-9f20-fb858dbc57d4)



## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

![Screenshot 2024-10-01 222428](https://github.com/user-attachments/assets/df99ab52-ad1f-432d-b799-af3a7d5a474c)

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
![image](https://github.com/user-attachments/assets/3819ca76-0831-4d7e-9346-b8eaaa554441)


## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
SLI stand for Service-Level Indicator is a specific metric used to measure the performance of a service.

 - SLO of monthly uptime and request response time:
   99.95% uptime in a month
   95% of requests should respond within 300 milliseconds
 - SLIs:
   Service was down for 22 minutes in a month
   95% of requests are processed within 250 milliseconds


## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
1. Uptime Percentage: This metric indicates the proportion of time the service is operational and available to users over a defined period
2. Average Response Time: This metric measures the average time taken to respond to user requests over a specified period.
3. Error Rate: This metric tracks the percentage of failed requests (e.g., HTTP 500 errors) compared to total requests.
4. 95th Percentile Response: his metric captures the response time below which 95% of requests fall. It helps identify outliers and ensures that the majority of users experience acceptable performance
5. Latency Distribution: This metric provides a breakdown of response times across different percentiles (e.g., 50th, 75th, 90th, 95th, and 99th). It helps visualize how response times vary and identify trends over time.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.
![image](https://github.com/user-attachments/assets/506aa731-ddf0-4280-9a42-8ffa6be329df)


## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.
![image](https://github.com/user-attachments/assets/5f657b1f-ca78-4085-a7ee-a791efcec156)


## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
![image](https://github.com/user-attachments/assets/7e591cd2-f16a-4e09-a608-028b1d2e3238)


## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name: Vo Minh Phong

Date: 5/10/2024

Subject:  Can't add star

Affected Area: Backend Uptime SLO

Severity: Hight

Description: We see increasing in 400 errors in backend service while calling service endpoint /star, That's might be bug or configuration issue We should solve this issue since it's affecting our target SLI is 4xx/5xx less then 0.5%


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.
 - Availability
 - Error Rate
 - Uptime Percentage
 - Successful Request Rate

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.
 * Uptime Percentage
   - This KPI measures the percentage of time the application is operational and accessible to users
 * Error Rate
   - This KPI measures the percentage of requests that result in errors (e.g., 4xx and 5xx HTTP status codes). It provides insight into the reliability of the application.
 * Average Response Time
   - This KPI tracks the average time taken to respond to user requests. It can be measured in milliseconds and should align with your SLO for response times.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

 * Frontend Avg Response time
   - This chart shows Average response time for frontend service, Which should not exceed 200 ms per-second
 * Backend Avg Response time
   - This chart shows Average response time for backend service, Which should not exceed 200 ms per-second
 * Application Memory usage
   - Show Memory used by our front-end and back-end services
 * CPU Usage
   - Should CPU used by our front-end and back-end services
 * Count Error
   - Show number error of back-end services

![image](https://github.com/user-attachments/assets/1aa58b7d-ee88-4b80-b40f-6db36d14ecbe)

