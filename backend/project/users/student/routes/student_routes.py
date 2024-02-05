import json
from flask import make_response
from flask import request, jsonify
import bson.json_util as json_util
import jwt
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

            # Generate JWT token
            token = jwt.encode({'user': user}, 'ssss', algorithm='HS256')

            # Create an HTTP-only cookie
            resp = make_response(jsonify({"message": message['message'], "user": user}))
            resp.set_cookie('access_token', token, httponly=True)
            return resp, 200
        else:
            return jsonify({"message": message, "code": status_code}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/users/student/<id>', methods=['GET'])
def get_student_by_id(id):
    try:
        student_instance = Student(collection_name="students")
        response = student_instance.get_user_by_id(id)
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
        if 'user' in session:
            user_id = session['user']
            student_instance = Student(collection_name="students")
            response = student_instance.get_student_by_id(user_id)
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


@app.route('/users/student/logout', methods=['POST'])
def student_logout():
    try:
        if 'user' in session:
            session.pop('user', None)
            return jsonify({"message": "Logout successful"}), 200
        else:
            return jsonify({"message": "User not authenticated"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/student/update', methods=['PUT'])
def update_user_profile():
    try:
        if 'user' in session:
            user_id = session['user']
            data = request.json

            student_instance = Student(collection_name="students")
            response = student_instance.update_student(user_id, data)

            if response.get("error"):
                return jsonify({"error": response["error"]}), 400
            elif response.get("message"):
                return jsonify({"message": response["message"]}), 200
            else:
                return jsonify({"message": "Update failed"}), 500
        else:
            return jsonify({"message": "User not authenticated"}), 401

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/users/student/update<id>', methods=['PUT'])
def update_user_student(id):
    return 'Hello World!'


@app.route('/users/student/delete/<id>', methods=['DELETE'])
def delete_user_student(id):
    return 'Hello World!'
