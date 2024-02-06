from app import database_client
import datetime

from bson.objectid import ObjectId


class InternshipSpaces:
    internship_spaces_collection = database_client['Project']['internship_spaces']

    def __init__(self, data):
        self.name = data['name']
        self.promotion = data['promotion']
        self.tutors_instruction = data['tutors_instruction']
        self.students_instruction = data['students_instruction']
        self.start_submission_date = datetime.datetime(data['startSubmissionDate'][0],
                                                       data['startSubmissionDate'][1],
                                                       data['startSubmissionDate'][2])
        self.end_submission_date = datetime.datetime(data['endSubmissionDate'][0],
                                                     data['endSubmissionDate'][1],
                                                     data['endSubmissionDate'][2])

    def jsonify(self):
        return {
            'name': self.name,
            'promotion': self.promotion,
            'tutors_instruction': self.tutors_instruction,
            'students_instruction': self.students_instruction,
            'startSubmissionDate': self.start_submission_date,
            'endSubmissionDate': self.end_submission_date
        }

    @staticmethod
    def return_format(internship_space):
        return {
            "id": str(internship_space["_id"]),
            "name": internship_space["name"],
            "promotion": internship_space["promotion"],
            "students_instruction": internship_space["students_instruction"],
            "tutors_instruction": internship_space["tutors_instruction"],
            "startSubmissionDate": internship_space["startSubmissionDate"].date().isoformat(),
            "endSubmissionDate": internship_space["endSubmissionDate"].date().isoformat()
        }

    @staticmethod
    def create_internship_spaces(data):
        new_internship_spaces = InternshipSpaces(data)

        response = InternshipSpaces.internship_spaces_collection.insert_one(new_internship_spaces.jsonify())
        return {'message': 'Internship spaces successfully created', 'inserted_id': str(response.inserted_id)}, 201

    @staticmethod
    def get_all_internship_spaces():

        internship_spaces = InternshipSpaces.internship_spaces_collection.find()

        transformed_internship_spaces = \
            [InternshipSpaces.return_format(internship_space) for internship_space in internship_spaces]

        return transformed_internship_spaces, 200

    @staticmethod
    def get_internship_spaces(internship_space_id):
        internship_space = InternshipSpaces.internship_spaces_collection.find_one(
            {'_id': ObjectId(internship_space_id)})
        if internship_space:
            transformed_internship_space = InternshipSpaces.return_format(internship_space)
            return transformed_internship_space, 200
        else:
            return {'message': 'Internship space not found'}, 404

    @staticmethod
    def edit_internship_spaces(internship_space_id, data):
        updated_internship_spaces = InternshipSpaces(data)
        update_result = InternshipSpaces.internship_spaces_collection.update_one({
            '_id': ObjectId(internship_space_id)}, {
            '$set': updated_internship_spaces.jsonify()
        })
        if update_result.matched_count and update_result.modified_count:
            return {'message': 'Internship spaces found and modified'}, 200
        elif update_result.matched_count and not update_result.modified_count:
            return {'message': 'Internship spaces unmodified'}, 204
        else:
            return {'message': 'Resource not found'}, 404

    @staticmethod
    def delete_internship_spaces(internship_id):
        delete_result = InternshipSpaces.internship_spaces_collection.delete_one({'_id': ObjectId(internship_id)})
        if delete_result.deleted_count:
            return {'message': 'Internship spaces successfully deleted'}, 200
        else:
            return {'message': 'Internship spaces not found'}, 204
