import json

from flask import request, jsonify
import bson.json_util as json_util
from company_tutor.models.company_tutor_model import CompanyTutor
from app import app
@app.route('/user/company-tutor/signin', methods=['POST'])
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


@app.route('/user/company-tutor/login', methods=['POST'])
def company_tutor_log_in():
    try:
        data = request.json
        company_tutor_instance = CompanyTutor(collection_name="academic_tutors")
        response = company_tutor_instance.company_tutor_log_in(data)
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


@app.route('/user/tutorEntreprise', methods=['POST'])
def add_user_tutor_entreprise():
    return 'Hello World!'


@app.route('/user/tutorEntreprise/<id>', methods=['GET'])
def get_user_tutor_entreprise(id):
    return 'Hello World!'


@app.route('/user/tutorEntreprise/<id>', methods=['PUT'])
def update_user_tutor_entreprise(id):
    return 'Hello World!'


@app.route('/user/tutorEntreprise/<id>', methods=['DELETE'])
def delete_user_tutor_entreprise(id):
    return 'Hello World!'
