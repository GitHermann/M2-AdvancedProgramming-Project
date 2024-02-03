from abc import ABC

from abstractUserModel.user_model import User


class AcademicTutor(User, ABC):

    def create_academic_tutor(self, data):
        return self.create_user(data)

    def academic_tutor_log_in(self, data):
        return self.user_log_in(data)

    def get_additional_fields(self, data):
        return {"academic_tutor_id": data['academic_tutor_id']}

    def get_academic_tutor_by_id(self, academic_tutor_id):
        return self.get_user_by_id(academic_tutor_id)