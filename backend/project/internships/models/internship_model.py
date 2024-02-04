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
    internship_spaces_collection = database_client['Project']['internship_spaces']

    def __init__(self, data, internship_space_id):
        self.title = data['title']
        self.startDate = datetime.datetime(data['startDate'][0], data['startDate'][1], data['startDate'][2])
        self.endDate = datetime.datetime(data['endDate'][0], data['endDate'][1], data['endDate'][2])
        self.company = data['company']
        self.student = session['user']
        self.academicTutor = data['academicTutor']
        self.companyTutor = data['companyTutor']
        self.internshipSpace = internship_space_id
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
            'internshipSpace': ObjectId(self.internshipSpace),
            'status': self.status.value
        }

    @staticmethod
    def createInternship(data, internship_space_id):
        internshipSpace = Internship.internship_spaces_collection.find_one({'_id': ObjectId(internship_space_id)})
        if internshipSpace:
            newInternship = Internship(data, internship_space_id)
            existingInternship = Internship.internships_collection.find_one(
            {'internshipSpace': ObjectId(newInternship.internshipSpace), 'student': ObjectId(newInternship.student)})
            if existingInternship:
                return {'message': 'Stage déjà créé'}, 400
            response = Internship.internships_collection.insert_one(newInternship.jsonify())
            return {'message': 'Internship successfully created', 'inserted_id': str(response.inserted_id)}, 201
        else:
            return {'message': 'Internship space not found'}, 404


    @staticmethod
    def getInternship(id, internship_space_id):
        internshipSpace = Internship.internship_spaces_collection.find_one({'_id': ObjectId(internship_space_id)})
        if internshipSpace:
            internship = Internship.internships_collection.find_one({'_id': ObjectId(id)})
            if internship:
                return internship, 200
            else:
                return {'message': 'Internship not found'}, 404
        else:
            return {'message': 'Internship space not found'}, 404
        
    @staticmethod
    def deleteInternship(id, internship_space_id):
        internshipSpace = Internship.internship_spaces_collection.find_one({'_id': ObjectId(internship_space_id)})
        if internshipSpace:
            deleteResult = Internship.internships_collection.delete_one({'_id': ObjectId(id)})
            if deleteResult.deleted_count:
                return {'message': 'Internship successfully deleted'}, 200
            else:
                return {'message': 'Internship not found'}, 204
        else:
            return {'message': 'Internship space not found'}, 404
        

