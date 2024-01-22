from flask import request, jsonify

from project.app import app
from users.student.models.student_model import Student


@app.route('/user/student/sign_in', methods=['POST'])
def student_sign_in():
    try:
        data = request.json
        response = Student.create_student(data)
        return jsonify({"message": "users added successfully", "user_id": str(response.inserted_id)}), 201

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
