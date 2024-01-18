from flask import Flask, jsonify
import os
import configparser

from db import get_db

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),".ini"))

# create and initialize a new Flask app
app = Flask(__name__)

database_client = get_db()

# Check if the connection is successful
if database_client:
    # Access the 'Users' collection in the 'Project' database
    project_db = database_client["Project"]
    users_collection = project_db["Users"]

else:
    print("Failed to connect to MongoDB.")

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/user', methods=['GET'])
def add_user():
    try:

        name = "Marc Evans"
        address = "Raimon"

        # Insert the user data into the 'Users' collection
        user_data = {"name": name, "address": address}
        result = users_collection.insert_one(user_data)

        return jsonify({"message": "User added successfully", "user_id": str(result.inserted_id)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config['PROD']['DB_URI']
    app.run()