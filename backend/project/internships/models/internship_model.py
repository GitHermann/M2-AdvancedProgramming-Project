from project.app import database_client
import datetime

class Internship:
  internships_collection = database_client['Project']['Internships']

  def __init__(self, data):
    self.title = data['title']
    self.startDate = datetime.datetime(data['startDate'][0],data['startDate'][1],data['startDate'][2])
    self.endDate = datetime.datetime(data['endDate'][0],data['endDate'][1],data['endDate'][2])
    self.company = data['company']
    self.student = data['student']
    self.academicTutor = data['academicTutor']
    self.companyTutor = data['companyTutor']
    self.internshipSpace = data['internshipSpace']

  def jsonify(self):
    return {
      'title': self.title,
      'startDate': self.startDate,
      'endDate': self.endDate,
      'company': self.company,
      'student': self.student,
      'academicTutor': self.academicTutor,
      'companyTuto': self.companyTutor,
      'internshipSpace': self.internshipSpace
    }

  @staticmethod
  def createInternship(data):
    newInternship = Internship(data)
    existingInternship = Internship.internships_collection.find_one({'internshipSpace': newInternship.internshipSpace, 'student': newInternship.student})
    if existingInternship:
      return {'message': 'Stage déjà créé'}, 400
    
    Internship.internships_collection.insert_one(newInternship.jsonify())
    return {'message': 'internship successfully created'}

