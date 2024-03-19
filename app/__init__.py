from flask import Flask
from .api import register_api_blueprints

app = Flask(__name__)

register_api_blueprints(app)
