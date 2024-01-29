from app import database_client
import datetime

from bson.objectid import ObjectId

class InternshipsSpace:
  internshipsSpace_collection = database_client['Project']['internships_space']

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
  def createIntershipsSpace(data):
    newInternshipsSpace = InternshipsSpace(data)
    
    InternshipsSpace.internshipsSpace_collection.insert_one(newInternshipsSpace.jsonify())
    return {'message': 'Interships space successfully created'}, 201
  
  @staticmethod
  def getAllInternshipsSpace():
    return [x for x in InternshipsSpace.internshipsSpace_collection.find()], 201
  
  @staticmethod
  def getInternshipsSpace(id):
    internshipsSpace = InternshipsSpace.internshipsSpace_collection.find_one({'_id': ObjectId(id)})
    if internshipsSpace:
      return internshipsSpace, 200
    else:
      return {'message': 'Resource not found'}, 404
    
  @staticmethod
  def editInternshipsSpace(id, data):
    updatedInternshipsSpace = InternshipsSpace(data)
    updateResult = InternshipsSpace.internshipsSpace_collection.update_one({'_id': ObjectId(id)}, { '$set': updatedInternshipsSpace.jsonify()})
    if updateResult.matched_count and updateResult.modified_count:
      return {'message': 'Internships space found and modified'}, 200
    elif updateResult.matched_count and not updateResult.modified_count:
      return {'message': 'Internships space unmodified'}, 204
    else:
      return {'message': 'Resource not found'}, 404
    
  
  @staticmethod
  def deleteInternshipsSpace(id):
    deleteResult = InternshipsSpace.internshipsSpace_collection.delete_one({'_id': ObjectId(id)})
    if deleteResult.deleted_count:
      return {'message': 'Internships space successfully deleted'}, 200
    else:
      return {'message': 'Internships space not found'}, 204 