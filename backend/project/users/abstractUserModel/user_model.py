from abc import ABC, abstractmethod
import bcrypt
from app import database_client
from bson import ObjectId


class User:
    def __init__(self, collection_name):
        self.users_collection = database_client["Project"][collection_name]

    def create_user(self, data):
        existing_user = self.users_collection.find_one({'email': data['email']})
        if existing_user:
            return {'message': 'User already exists'}, 400

        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        new_user = {
            'username': data['username'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': hashed_password,
            'phone': data['phone']
        }
        new_user.update(self.get_additional_fields(data))
        self.users_collection.insert_one(new_user)
        new_user.pop('password')
        return {'message': 'Sign In successful', 'user': new_user}, 201

    def user_log_in(self, data):
        if 'email' not in data or 'password' not in data:
            return {'message': 'Missing email or password'}, 400

        existing_user = self.users_collection.find_one(
            {'email': data['email']})

        if existing_user and bcrypt.checkpw(data['password'].encode('utf8'), existing_user['password']):
            return {'message': 'Login successful',  'user': existing_user}, 200
        else:
            return {'message': 'Invalid email or password'}, 400

    def get_user_by_id(self, user_id):
        user_data = self.users_collection.find_one({"_id": ObjectId(user_id)})
        if user_data:
            return {'user': user_data}, 200
        else:
            return {'message': 'User does not exist'}, 404

    @abstractmethod
    def get_additional_fields(self, data):
        pass
