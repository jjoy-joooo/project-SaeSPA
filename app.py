from flask import Flask
from app.api import register_api_blueprints

app = Flask(__name__)

register_api_blueprints(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
