from abc import ABC

from users.abstractUserModel.user_model import User


class CompanyTutor(User, ABC):

    def create_company_tutor(self, data):
        return self.create_user(data)

    def company_tutor_log_in(self, data):
        return self.user_log_in(data)

    def get_additional_fields(self, data):
        return {"company_tutor_id": data['company_tutor_id']}
