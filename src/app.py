import logging
import uuid
from flask import Flask, g, request
from flask_migrate import Migrate

from src.libs.config import Config
from src.libs.db import db
from src.libs.request_logger import setup_request_logging
from src.libs.error_handler import register_error_handlers

from src.api.items_api import api as itemsApi

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(itemsApi, url_prefix='/api')
    setup_request_logging(app)
    register_error_handlers(app)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)
