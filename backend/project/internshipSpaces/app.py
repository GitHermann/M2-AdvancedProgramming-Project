from flask import Flask
from flask_cors import CORS
import os
import configparser

from db import get_db

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), ".ini"))

app = Flask(__name__)

CORS(
    app,
    resources={r"/*": {"origins": ["https://my-internships.com", "http://localhost:8082"]}}
)

mongo_uri = config['PROD']['DB_URI']
database_client = get_db(mongo_uri)

secret_key = os.urandom(12).hex()
app.config['SECRET_KEY'] = secret_key

import importAllRoutes


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=5002)
