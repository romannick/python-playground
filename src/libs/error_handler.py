from flask import jsonify
from src.libs.exceptions import NotFound, BadRequest

def register_error_handlers(app):
    @app.errorhandler(NotFound)
    def handle_not_found(error):
        response = jsonify({"error": str(error)})
        response.status_code = 404
        return response

    @app.errorhandler(BadRequest)
    def handle_bad_request(error):
        response = jsonify({"error": str(error)})
        response.status_code = 400
        return response