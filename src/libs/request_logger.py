import logging
import uuid
from flask import g, request

class TraceIdFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = getattr(g, "trace_id", "N/A")
        return True

def setup_request_logging(app):
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '[%(asctime)s] [TRACE_ID=%(trace_id)s] %(levelname)s in %(module)s: %(message)s'
    )
    handler.setFormatter(formatter)
    handler.addFilter(TraceIdFilter())

    app.logger.handlers = []
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    logging.getLogger().addFilter(TraceIdFilter())

    @app.before_request
    def assign_trace_id():
        g.trace_id = str(uuid.uuid4())
        app.logger.info(f"Incoming request: {request.method} {request.path}")

    @app.after_request
    def log_response(response):
        app.logger.info(f"Completed {request.method} {request.path} -> {response.status}")
        return response
