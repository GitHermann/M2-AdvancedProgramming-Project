import json
from flask import request, jsonify
import bson.json_util as json_util

from admin.models.admin_model import Admin
from app import app, session


@app.route('/users/admin/signin', methods=['POST'])
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


@app.route('/users/admin/login', methods=['POST'])
def admin_log_in():
    try:
        data = request.json
        admin_instance = Admin(collection_name="admins")
        response = admin_instance.admin_log_in(data)
        message, status_code = response
        if status_code == 200:
            user = json.loads(json_util.dumps(message['user']))
            session['user'] = user["_id"]["$oid"]
            return jsonify({"message": message['message'], "user": user}), 200
        else:
            return jsonify({"message": message['message'], "code": status_code}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/admin/logout', methods=['POST'])
def admin_logout():
    try:
        if 'user' in session:
            session.pop('user', None)
            return jsonify({"message": "Logout successful"}), 200
        else:
            return jsonify({"message": "User not authenticated"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/admin/<id>', methods=['GET'])
def get_admin_by_id(admin_id):
    try:
        admin_instance = Admin(collection_name="admins")
        response = admin_instance.get_user_by_id(admin_id)
        user_data, status_code = response
        if user_data and status_code == 200:
            user_data['user'].pop('password', None)
            user = json.loads(json_util.dumps(user_data['user']))
            return jsonify({"user": user}), 200
        else:
            return jsonify({"message": "User not found"}), 404

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/admin/profile', methods=['GET'])
def get_authenticated_admin_profile():
    try:
        if 'user' in session:
            user_id = session['user']
            admin_instance = Admin(collection_name="admins")
            response = admin_instance.get_admin_by_id(user_id)
            user_data, status_code = response
            if user_data and status_code == 200:
                user = json.loads(json_util.dumps(user_data['user']))
                user_data.pop('password', None)
                return jsonify({"user": user}), 200
            else:
                return jsonify({"message": "User not found"}), 404
        else:
            return jsonify({"message": "User not authenticated"}), 401

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
