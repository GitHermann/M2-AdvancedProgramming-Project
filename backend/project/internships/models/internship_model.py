from app import database_client, session
import datetime
from bson.objectid import ObjectId
from enum import Enum

INTERNSHIP_SPACE_NOT_FOUND_ERROR = 'Internship space not found'
INTERNSHIP_NOT_FOUND_ERROR = 'Internship not found'


class ValidationStatus(Enum):
    ONGOING = 0
    VALIDATED = 1
    REJECTED = 2


class Internship:
    internships_collection = database_client['Project']['internships']
    internship_spaces_collection = database_client['Project']['internship_spaces']

    def __init__(self, data, internship_space_id, student_id):
        self.title = data['title']
        self.start_date = datetime.datetime(data['startDate'][0], data['startDate'][1], data['startDate'][2])
        self.end_date = datetime.datetime(data['endDate'][0], data['endDate'][1], data['endDate'][2])
        self.company = data['company']
        self.student_id = student_id
        self.academic_tutor = data['academicTutor']
        self.company_tutor = data['companyTutor']
        self.internship_space = internship_space_id
        self.status = ValidationStatus.ONGOING

    def jsonify(self):
        return {
            'title': self.title,
            'startDate': self.start_date,
            'endDate': self.end_date,
            'company': self.company,
            'studentId': ObjectId(self.student_id),
            'academicTutor': self.academic_tutor,
            'companyTutor': self.company_tutor,
            'internshipSpace': ObjectId(self.internship_space),
            'status': self.status.value
        }

    @staticmethod
    def return_format(internship):
        status = str()
        match (internship["status"]):
            case 0:
                status = "En cours de validation"
            case 1:
                status = "Validé"
            case 2:
                status = "Rejeté"

        return {
            "id": str(internship["_id"]),
            "studentId": str(internship["studentId"]),
            "academicTutor": internship["academicTutor"],
            "company": internship["company"],
            "companyTutor": internship["companyTutor"],
            "startDate": internship["startDate"].date().isoformat(),
            "endDate": internship["endDate"].date().isoformat(),
            "internshipSpace": str(internship["internshipSpace"]),
            "status": status,
            "title": internship["title"]
        }

    @staticmethod
    def create_internship(data, internship_space_id, student_id):
        internship_space = Internship.internship_spaces_collection.find_one({'_id': ObjectId(internship_space_id)})
        if internship_space:
            new_internship = Internship(data, internship_space_id, student_id)
            existing_internship = Internship.internships_collection.find_one(
                {'internshipSpace': ObjectId(new_internship.internship_space), 'studentId': ObjectId(student_id)})
            if existing_internship:
                return {'message': 'Stage déjà créé'}, 400
            response = Internship.internships_collection.insert_one(new_internship.jsonify())
            return {'message': 'Internship successfully created', 'inserted_id': str(response.inserted_id)}, 201
        else:
            return {'message': INTERNSHIP_SPACE_NOT_FOUND_ERROR}, 404

    @staticmethod
    def get_internship(internship_id, internship_space_id):
        internship_space = Internship.internship_spaces_collection.find_one({'_id': ObjectId(internship_space_id)})
        if internship_space:
            filter_condition = {
                '$or': [
                    {'_id': ObjectId(internship_id)},
                    {'studentId': ObjectId(internship_id)}
                ]
            }
            internship = Internship.internships_collection.find_one(filter_condition)
            if internship:
                return Internship.return_format(internship), 200
            else:
                return {'message': INTERNSHIP_NOT_FOUND_ERROR}, 404
        else:
            return {'message': INTERNSHIP_SPACE_NOT_FOUND_ERROR}, 404

    @staticmethod
    def get_all_internships_in_space(internship_space_id):
        internship_space = Internship.internship_spaces_collection.find_one({'_id': ObjectId(internship_space_id)})
        if internship_space:
            internships = Internship.internships_collection.find({'internshipSpace': ObjectId(internship_space_id)})
            if internships:
                return [Internship.return_format(internship) for internship in internships], 200
        else:
            return {'message': INTERNSHIP_SPACE_NOT_FOUND_ERROR}, 404

    @staticmethod
    def set_status(internship_id, status):
        updated_internship = Internship.internships_collection.find_one_and_update({'_id': ObjectId(internship_id)},
                                                                                   {'$set': {'status': status}})
        if updated_internship:
            return updated_internship, 200
        else:
            return {'message': INTERNSHIP_NOT_FOUND_ERROR}, 404

    @staticmethod
    def delete_internship(internship_id, internship_space_id):
        internship_space = Internship.internship_spaces_collection.find_one({'_id': ObjectId(internship_space_id)})
        if internship_space:
            delete_result = Internship.internships_collection.delete_one({'_id': ObjectId(internship_id)})
            if delete_result.deleted_count:
                return {'message': 'Internship successfully deleted'}, 200
            else:
                return {'message': INTERNSHIP_NOT_FOUND_ERROR}, 204
        else:
            return {'message': INTERNSHIP_SPACE_NOT_FOUND_ERROR}, 404
