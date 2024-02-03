import gridfs
from app import database_client
from bson.objectid import ObjectId


class AbstractDocument:
    def __init__(self, collection_name, data):
        self.documents_collection = database_client["Project"][collection_name]
        self.internship = ObjectId(data["internship"])
        self.document_name = data['document_name']
        self.level_of_confidentiality = data.get('level_of_confidentiality', '')

    def jsonify(self):
        return {
            'internship': self.internship,
            'document_name': self.document_name,
            'level_of_confidentiality': self.level_of_confidentiality
        }

    def save_file(self, file_data, filename, collection_name):
        fs = gridfs.GridFS(self.documents_collection.database, collection=collection_name)
        file_id = fs.put(file_data, filename=filename)
        return file_id

    def create_document(self, collection_name, data, file_data):
        new_document = AbstractDocument(collection_name, data)
        existing_document = self.documents_collection.find_one(
            {'document_name': new_document.document_name, 'internship': new_document.internship})
        if existing_document:
            return {'message': 'Document already exists'}, 400

        file_id = new_document.save_file(file_data, new_document.document_name, collection_name)

        new_document.jsonify()['file_id'] = file_id

        self.documents_collection.insert_one(new_document.jsonify())
        return {'message': 'Document successfully created'}, 201
