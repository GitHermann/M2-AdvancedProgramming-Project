from abc import ABC

from abstractUserModel.user_model import User


class Admin(User, ABC):

    def create_admin(self, data):
        return self.create_user(data)

    def admin_log_in(self, data):
        return self.user_log_in(data)

    def get_additional_fields(self, data):
        return {"test": data['test']}

    def get_admin_by_id(self, admin_id):
        return self.get_user_by_id(admin_id)