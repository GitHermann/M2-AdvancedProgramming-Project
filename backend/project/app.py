from flask import Flask, jsonify, session
from flask_cors import CORS
import project.users.abstractUserModel
import os
import configparser

from project.db import get_db

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), ".ini"))

# create and initialize a new Flask app
app = Flask(__name__)
CORS(app)

# Get the MongoDB URI from the config file
mongo_uri = config['PROD']['DB_URI']

# Initialize the database client
database_client = get_db(mongo_uri)

# Initialize secret key
secret_key = os.urandom(12).hex()
app.config['SECRET_KEY'] = secret_key

import project.importAllRoutes


@app.route("/")
def hello():
    #Placeholder
    session['user'] = '65b12927b91ba67d6de2eaad'
    return "Hello, World!"


@app.route('/test', methods=['GET'])
def add_user():
    try:
        name = "Marc Evans"
        address = "Raimon"

        # Insert the user data into the 'users' collection
        user_data = {"name": name, "address": address}
        result = database_client["Project"]["users"].insert_one(user_data)

        return jsonify({"message": "users added successfully", "user_id": str(result.inserted_id)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()
