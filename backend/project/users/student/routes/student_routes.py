import json

from flask import request, jsonify
import bson.json_util as json_util

from project.users.student.models.student_model import Student
from project.app import app, session


@app.route('/user/student/signin', methods=['POST'])
def student_sign_in():
    try:
        data = request.json
        student_instance = Student(collection_name="students")
        response = student_instance.create_student(data)
        return jsonify({"message": str(response)}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/student/login', methods=['POST'])
def student_log_in():
    try:
        data = request.json
        student_instance = Student(collection_name="students")
        response = student_instance.student_log_in(data)
        # Serialization of ObjectID from user
        user = json.loads(json_util.dumps(response['user']))
        session['user'] = user["_id"]["$oid"]
        if response['code'] == 201:
            return jsonify({"message": response['message'], "user": user}), 201
        else:
            return jsonify({"message": response['message']}), 401

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/student', methods=['POST'])
def add_user_student():
    return 'Hello World!'


@app.route('/user/student/<id>', methods=['GET'])
def get_user_student(id):
    return 'Hello World!'


@app.route('/user/student/<id>', methods=['PUT'])
def update_user_student(id):
    return 'Hello World!'


@app.route('/user/student/<id>', methods=['DELETE'])
def delete_user_student(id):
    return 'Hello World!'
