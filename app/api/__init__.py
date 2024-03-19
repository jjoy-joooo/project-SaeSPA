from flask import Flask

from .text_extraction_api import text_extraction_blueprint

def register_api_blueprints(app: Flask):
    app.register_blueprint(text_extraction_blueprint, url_prefix='/api/text_extraction')

