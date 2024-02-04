from abc import abstractmethod

import gridfs

from bson.objectid import ObjectId


class AbstractDocument:
    def __init__(self, data):
        self.internship = ObjectId(data["internship"])
        self.document_name = data['document_name']
        self.level_of_confidentiality = data.get('level_of_confidentiality', '')

    def jsonify(self):
        return {
            'internship': self.internship,
            'document_name': self.document_name,
            'level_of_confidentiality': self.level_of_confidentiality
        }

    def save_file(self, file_data, filename, database, collection_name, data_body):
        fs = gridfs.GridFS(database, collection=collection_name)
        file_id = fs.put(file_data, filename=filename, metadata=data_body)
        return file_id

    @abstractmethod
    def create_document(self, data, file_data):
        pass

    @abstractmethod
    def get_document(self, file_id):
        pass

    @abstractmethod
    def delete_document(self, file_id):
        pass
