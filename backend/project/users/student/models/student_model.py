import bcrypt

from abc import ABC

from abstractUserModel.user_model import User


def get_additional_fields(data):
    return {"student_id": data['student_id'], "promotion": data['promotion']}


class Student(User):
    def create_student(self, data):
        if data['email'].endswith('@efrei.net'):
            return self.create_user(data)
        else:
            return 'Wrong email structure'

    def student_log_in(self, data):
        return self.user_log_in(data)

    def get_student_by_id(self, student_id):
        return self.get_user_by_id(student_id)
