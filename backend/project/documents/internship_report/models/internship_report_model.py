from asbtract_document_model.document_model import AbstractDocument
from app import database_client


class InternshipReport(AbstractDocument):
    internships_reports_collection = database_client['Project']['internships_reports']

    def __init__(self, data, file_data):
        super().__init__(data)
        self.file = file_data

    def create_document(self, data, file_data):
        new_document = InternshipReport(data, file_data)
        existing_document = InternshipReport.internships_reports_collection.find_one(
            {'document_name': new_document.document_name, 'internship': new_document.internship})
        if existing_document:
            return {'message': 'Document already exists'}, 400

        file_id = new_document.save_file(file_data, new_document.document_name,
                                         self.internships_reports_collection.database, 'internships_reports', data)

        new_document.jsonify()['file_id'] = file_id

        return {'message': 'Document successfully created'}, 201
