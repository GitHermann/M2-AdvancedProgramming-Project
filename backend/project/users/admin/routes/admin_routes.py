import json
from flask import request, jsonify
import bson.json_util as json_util

from project.users.admin.models.admin_model import Admin
from __main__ import app

@app.route('/user/admin/signin', methods=['POST'])
def admin_sign_in():
    try:
        data = request.json
        admin_instance = Admin(collection_name="admins")
        response = admin_instance.create_admin(data)
        return jsonify({"message": str(response)}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/admin/login', methods=['POST'])
def admin_log_in():
    try:
        data = request.json
        admin_instance = Admin(collection_name="admins")
        response = admin_instance.admin_log_in(data)
        # Serialization of ObjectID from user
        user = json.loads(json_util.dumps(response['user']))
        if response['code'] == 201:
            return jsonify({"message": response['message'], "user": user}), 201
        else:
            return jsonify({"message": response['message']}), 401

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/user/admin', methods=['POST'])
def add_user_admin():
    return 'Hello World!'


@app.route('/user/admin/<id>', methods=['GET'])
def get_user_admin(id):
    return 'Hello World!'


@app.route('/user/admin/<id>', methods=['PUT'])
def update_user_admin(id):
    return 'Hello World!'


@app.route('/user/admin/<id>', methods=['DELETE'])
def delete_user_admin(id):
    return 'Hello World!'
