from abc import ABC, abstractmethod
import bcrypt
from app import database_client


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
            'phone': data['phone'],
        }
        new_user.update(self.get_additional_fields(data))
        self.users_collection.insert_one(new_user)
        return {'message': 'Sign In successful', 'user': new_user}, 201

    def user_log_in(self, data):
        # Validation des données
        if 'email' not in data or 'password' not in data:
            return {'message': 'Missing email or password'}, 400

        existing_user = self.users_collection.find_one(
            {'email': data['email']})

        if existing_user and bcrypt.checkpw(data['password'].encode('utf8'), existing_user['password']):
            return {'message': 'Login successful', 'code': 201, 'user': existing_user}
        else:
            return {'message': 'Invalid email or password', 'code': 401}

    @abstractmethod
    def get_additional_fields(self, data):
        pass
