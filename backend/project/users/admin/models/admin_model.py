from abc import ABC

from abstractUserModel.user_model import User


def get_additional_fields(data):
    return {"test": data['test']}


class Admin(User, ABC):

    def create_admin(self, data):
        if data['email'].endswith('@admin.efrei.net'):
            return self.create_user(data)
        else:
            return 'Wrong email structure'

    def admin_log_in(self, data):
        return self.user_log_in(data)

    def get_admin_by_id(self, admin_id):
        return self.get_user_by_id(admin_id)