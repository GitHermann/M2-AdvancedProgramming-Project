import bcrypt

from abc import ABC

from project.users.abstractUserModel.user_model import User


class Student(User):
    def create_student(self, data):
        return self.create_user(data)

    def student_log_in(self, data):
        return self.user_log_in(data)

    def get_additional_fields(self, data):
        return {"student_id": data['student_id'], "promotion": data['promotion']}
