from app import database_client
import datetime

from bson.objectid import ObjectId

class InternshipSpaces:
  internshipSpaces_collection = database_client['Project']['internship_spaces']

  def __init__(self, data):
    self.name = data['name']
    self.promotion = data['promotion']
    self.tutors_instruction = data['tutors_instruction']
    self.students_instruction = data['students_instruction']
    self.startSubmissionDate = datetime.datetime(data['startSubmissionDate'][0],data['startSubmissionDate'][1],data['startSubmissionDate'][2])
    self.endSubmissionDate = datetime.datetime(data['endSubmissionDate'][0],data['endSubmissionDate'][1],data['endSubmissionDate'][2])

  def jsonify(self):
    return {
      'name': self.name,
      'promotion': self.promotion,
      'tutors_instruction': self.tutors_instruction,
      'students_instruction': self.students_instruction,
      'startSubmissionDate': self.startSubmissionDate,
      'endSubmissionDate': self.endSubmissionDate
    }
  
  @staticmethod
  def createIntershipSpaces(data):
    newInternshipSpaces = InternshipSpaces(data)
    
    InternshipSpaces.internshipSpaces_collection.insert_one(newInternshipSpaces.jsonify())
    return {'message': 'Intership spaces successfully created'}, 201
  
  @staticmethod
  def getAllInternshipSpaces():
    return [x for x in InternshipSpaces.internshipSpaces_collection.find()], 201
  
  @staticmethod
  def getInternshipSpaces(id):
    internshipSpaces = InternshipSpaces.internshipSpaces_collection.find_one({'_id': ObjectId(id)})
    if internshipSpaces:
      return internshipSpaces, 200
    else:
      return {'message': 'Resource not found'}, 404
    
  @staticmethod
  def editInternshipSpaces(id, data):
    updatedInternshipSpaces = InternshipSpaces(data)
    updateResult = InternshipSpaces.internshipSpaces_collection.update_one({'_id': ObjectId(id)}, { '$set': updatedInternshipSpaces.jsonify()})
    if updateResult.matched_count and updateResult.modified_count:
      return {'message': 'Internship spaces found and modified'}, 200
    elif updateResult.matched_count and not updateResult.modified_count:
      return {'message': 'Internship spaces unmodified'}, 204
    else:
      return {'message': 'Resource not found'}, 404
    
  
  @staticmethod
  def deleteInternshipSpaces(id):
    deleteResult = InternshipSpaces.internshipSpaces_collection.delete_one({'_id': ObjectId(id)})
    if deleteResult.deleted_count:
      return {'message': 'Internship spaces successfully deleted'}, 200
    else:
      return {'message': 'Internship spaces not found'}, 204