from flask import Flask, jsonify
import os
import configparser

from project.db import get_db

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), ".ini"))

# create and initialize a new Flask app
app = Flask(__name__)

# Get the MongoDB URI from the config file
mongo_uri = config['PROD']['DB_URI']

# Initialize the database client
database_client = get_db(mongo_uri)

import project.importAllRoutes

@app.route("/")
def hello():
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
