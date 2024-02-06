from abc import ABC

from abstractUserModel.user_model import User


def get_additional_fields(data):
    return {"academic_tutor_id": data['academic_tutor_id']}


class AcademicTutor(User, ABC):

    def create_academic_tutor(self, data):
        if data['email'].endswith('@academictutor.efrei.net'):
            return self.create_user(data)
        else:
            return 'Wrong email structure'

    def academic_tutor_log_in(self, data):
        return self.user_log_in(data)

    def get_academic_tutor_by_id(self, academic_tutor_id):
        return self.get_user_by_id(academic_tutor_id)