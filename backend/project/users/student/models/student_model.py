import bcrypt

from project.app import database_client

students_collection = database_client["Project"]["students"]


class Student:
    @staticmethod
    def create_student(data):

        existing_user_student = students_collection.find_one({'email': data['email']})
        if existing_user_student:
            return {'message': 'Student already exists'}, 400

        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        new_student = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'student_id': data['student_id'],
            'password': hashed_password,
            'phone': data['phone'],
            'promotion': data['promotion']
        }
        students_collection.insert_one(new_student)
        return {'message': 'Sign In successful', 'user': new_student}, 201

    @staticmethod
    def student_log_in(data):
        existing_user_student = students_collection.find_one(
            {'email': data['email']})
        if existing_user_student and bcrypt.checkpw(data['password'].encode('utf8'),existing_user_student['password']):
            return {'message': 'Login successful', 'code': 201}
        else:
            return {'message': 'Invalid email or password', 'code': 401}

