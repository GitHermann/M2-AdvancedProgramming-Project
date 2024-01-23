from flask import request, jsonify

from project.app import app
from project.users.student.models.student_model import Student
from __main__ import app


@app.route('/user/student/signin', methods=['POST'])
def student_sign_in():
    try:
        data = request.json
        response = Student.create_student(data)
        return jsonify({"message": str(response)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/student/login', methods=['POST'])
def student_log_in():
    try:
        data = request.json
        response = Student.student_log_in(data)

        if response['code'] == 201:
            return jsonify({"message": response['message']}), 201
        else:
            return jsonify({"message": response['message']}), 401

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
