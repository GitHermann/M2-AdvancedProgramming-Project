from abc import ABC

from abstractUserModel.user_model import User


class CompanyTutor(User, ABC):

    def create_company_tutor(self, data):
        if data['email'].endswith('@companytutor.efrei.net'):
            return self.create_user(data)
        else:
            return 'Wrong email structure'

    def company_tutor_log_in(self, data):
        return self.user_log_in(data)

    def get_additional_fields(self, data):
        return {"company_tutor_id": data['company_tutor_id']}

    def get_company_tutor_by_id(self, company_tutor_id):
        return self.get_user_by_id(company_tutor_id)