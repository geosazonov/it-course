from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('credit_limit_processing_seconds', 'Time spent processing credit limit request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    limit = bool(random.getrandbits(1)) if 100000 else 5000
    print(limit)
    # do hard work
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8888)
    # Generate some requests.
    while True:
        process_request(random.random())
