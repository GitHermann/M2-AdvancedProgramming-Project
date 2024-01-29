import json
import bson.json_util as json_util
from flask import request, jsonify

from academic_tutor.models.academic_tutor_model import AcademicTutor
from app import app


@app.route('/users/academic-tutor/signin', methods=['POST'])
def academic_tutor_sign_in():
    try:
        data = request.json
        academic_tutor_instance = AcademicTutor(collection_name="academic_tutors")
        response = academic_tutor_instance.create_academic_tutor(data)
        return jsonify({"message": str(response)}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/academic-tutor/login', methods=['POST'])
def academic_tutor_log_in():
    try:
        data = request.json
        academic_tutor_instance = AcademicTutor(collection_name="academic_tutors")
        response = academic_tutor_instance.academic_tutor_log_in(data)
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


@app.route('/users/tutorAcademic', methods=['POST'])
def add_user_tutor_academic():
    return 'Hello World!'


@app.route('/users/tutorAcademic/<id>', methods=['GET'])
def get_user_tutor_academic(id):
    return 'Hello World!'


@app.route('/users/tutorAcademic/<id>', methods=['PUT'])
def update_user_tutor_academic(id):
    return 'Hello World!'


@app.route('/users/tutorAcademic/<id>', methods=['DELETE'])
def delete_user_tutor_academic(id):
    return 'Hello World!'
