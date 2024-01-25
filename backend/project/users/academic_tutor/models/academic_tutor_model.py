from abc import ABC

from project.users.abstractUserModel.user_model import User


class AcademicTutor(User, ABC):

    def create_academic_tutor(self, data):
        return self.create_user(data)

    def academic_tutor_log_in(self, data):
        return self.user_log_in(data)

    def get_additional_fields(self, data):
        return {"academic_tutor_id": data['academic_tutor_id']}
