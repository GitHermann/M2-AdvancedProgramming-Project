from abc import ABC

from abstractUserModel.user_model import User


class Admin(User, ABC):

    def create_admin(self, data):
        return self.create_user(data)

    def admin_log_in(self, data):
        return self.user_log_in(data)

    def get_additional_fields(self, data):
        return {"test": data['test']}
