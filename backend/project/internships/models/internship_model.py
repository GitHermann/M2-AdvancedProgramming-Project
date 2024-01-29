from app import database_client, session
import datetime
from bson.objectid import ObjectId
from enum import Enum


class ValidationStatus(Enum):
    ONGOING = 0
    VALIDATED = 1
    REJECTED = 2


class Internship:
    internships_collection = database_client['Project']['internships']

    def __init__(self, data):
        self.title = data['title']
        self.startDate = datetime.datetime(data['startDate'][0], data['startDate'][1], data['startDate'][2])
        self.endDate = datetime.datetime(data['endDate'][0], data['endDate'][1], data['endDate'][2])
        self.company = data['company']
        self.student = session['user']
        self.academicTutor = data['academicTutor']
        self.companyTutor = data['companyTutor']
        self.internshipSpace = data['internshipSpace']
        self.status = ValidationStatus.ONGOING

    def jsonify(self):
        return {
            'title': self.title,
            'startDate': self.startDate,
            'endDate': self.endDate,
            'company': self.company,
            'student': ObjectId(self.student),
            'academicTutor': self.academicTutor,
            'companyTuto': self.companyTutor,
            'internshipSpace': self.internshipSpace,
            'status': self.status.value
        }

    @staticmethod
    def createInternship(data):
        newInternship = Internship(data)
        existingInternship = Internship.internships_collection.find_one(
            {'internshipSpace': newInternship.internshipSpace, 'student': ObjectId(newInternship.student)})
        if existingInternship:
            return {'message': 'Stage déjà créé'}, 400

        Internship.internships_collection.insert_one(newInternship.jsonify())
        return {'message': 'internship successfully created'}, 201

    @staticmethod
    def getInternship(id):
        internship = Internship.internships_collection.find_one({'_id': ObjectId(id)})
        if internship:
            return internship, 200
        else:
            return {'message': 'Resource not found'}, 404
