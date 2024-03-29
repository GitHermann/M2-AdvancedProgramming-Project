import json

from flask import request, jsonify
import bson.json_util as json_util
from company_tutor.models.company_tutor_model import CompanyTutor
from app import app, session


@app.route('/users/company-tutor/signin', methods=['POST'])
def company_tutor_sign_in():
    try:
        data = request.json
        company_tutor_instance = CompanyTutor(collection_name="company_tutors")
        response = company_tutor_instance.create_company_tutor(data)
        return jsonify({"message": str(response)}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/company-tutor/login', methods=['POST'])
def company_tutor_log_in():
    try:
        data = request.json
        company_tutor_instance = CompanyTutor(collection_name="company_tutors")
        response = company_tutor_instance.company_tutor_log_in(data)
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


@app.route('/users/company-tutor/logout', methods=['POST'])
def company_tutor_logout():
    try:
        if 'user' in session:
            session.pop('user', None)
            return jsonify({"message": "Logout successful"}), 200
        else:
            return jsonify({"message": "User not authenticated"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/company-tutor/<id>', methods=['GET'])
def get_company_tutor_by_id(id):
    try:
        company_tutor_instance = CompanyTutor(collection_name="company_tutors")
        response = company_tutor_instance.get_user_by_id(id)
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


@app.route('/users/company-tutor/profile', methods=['GET'])
def get_authenticated_company_tutor_profile():
    try:
        if 'user' in session:
            user_id = session['user']
            company_tutor_instance = CompanyTutor(collection_name="company_tutors")
            response = company_tutor_instance.get_company_tutor_by_id(user_id)
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
