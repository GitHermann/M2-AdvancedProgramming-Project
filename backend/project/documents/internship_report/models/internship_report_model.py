import gridfs
from asbtract_document_model.document_model import AbstractDocument
from app import database_client
from bson import ObjectId
from flask import send_file


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

    def get_document(self, file_id):
        try:
            _id = ObjectId(file_id)
            fs = gridfs.GridFS(self.internships_reports_collection.database, collection='internships_reports')
            file_data = fs.get(_id)
            content_type = 'application/octet-stream'
            return send_file(file_data, mimetype=content_type, as_attachment=True, download_name=file_data.filename)

        except Exception as e:
            return {'error': str(e)}, 500

    def delete_document(self, file_id):
        try:
            file_id = ObjectId(file_id)

            fs = gridfs.GridFS(self.internships_reports_collection.database, collection='internships_reports')
            fs.delete(file_id)

            self.internships_reports_collection.delete_one({'file_id': file_id})

            return {'message': 'Document successfully deleted'}, 200

        except Exception as e:
            return {'error': str(e)}, 500
