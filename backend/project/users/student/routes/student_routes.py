import json
from flask import make_response
from flask import request, jsonify
import bson.json_util as json_util
import jwt
from datetime import datetime, timedelta
from student.models.student_model import Student
from app import app, session


@app.route('/users/student/signin', methods=['POST'])
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


@app.route('/users/student/login', methods=['POST'])
def student_log_in():
    try:
        data = request.json
        student_instance = Student(collection_name="students")
        response = student_instance.student_log_in(data)
        message, status_code = response
        if status_code == 200:
            user = json.loads(json_util.dumps(message['user'], default=str))
            user.pop('password', None)
            user['userId'] = user["_id"]["$oid"]
            user.pop('_id', None)

            token = jwt.encode({'user': user}, 'ssss', algorithm='HS256')

            resp = make_response(jsonify({"message": message['message'], "user": user}))
            resp.set_cookie('access_token', token, httponly=True, expires=datetime.now() + timedelta(days=30))
            return resp, 200
        else:
            return jsonify({"message": message, "code": status_code}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/student/<student_id>', methods=['GET'])
def get_student_by_id(student_id):
    try:
        student_instance = Student(collection_name="students")
        response = student_instance.get_user_by_id(student_id)
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


@app.route('/users/student/profile', methods=['GET'])
def get_authenticated_student_profile():
    try:
        token = request.cookies.get('access_token')

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        decoded_token = jwt.decode(token, 'ssss', algorithms=['HS256'])

        user_data = decoded_token.get('user')

        if not user_data:
            return jsonify({"error": "Invalid token"}), 401

        return jsonify({"user": user_data}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401

    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/student/logout', methods=['POST'])
def student_logout():
    try:
        resp = make_response(jsonify({"message": "Logout successful"}))
        resp.set_cookie('access_token', '', expires=0)
        return resp, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/student/<student_id>', methods=['PUT'])
def update_student_by_id(student_id):
    try:
        data = request.json
        student_instance = Student(collection_name="students")
        response = student_instance.update_user_by_id(student_id, data)
        message, status_code = response
        if status_code == 200:
            return jsonify({"message": message['message']}), 200
        else:
            return jsonify({"message": message['message'], "code": status_code}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/student/<student_id>', methods=['DELETE'])
def delete_student_by_id(student_id):
    try:
        student_instance = Student(collection_name="students")
        response = student_instance.delete_user_by_id(student_id)
        message, status_code = response
        if status_code == 200:
            return jsonify({"message": message['message']}), 200
        else:
            return jsonify({"message": message['message'], "code": status_code}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
