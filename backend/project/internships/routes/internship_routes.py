from flask import request, jsonify

from project.app import app
from project.internships.models.internship_model import Internship


@app.route('/internships', methods=['POST'])
def add_internship():
    try:
        data = request.json
        response = Internship.createInternship(data)
        return jsonify({"message": "Internship added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/internships/<id>', methods=['GET'])
def get_internship(id):
    return 'Hello World!'


@app.route('/internships/<id>', methods=['PUT'])
def update_internship(id):
    return 'Hello World!'

@app.route('/internships/<id>', methods=['DELETE'])
def delete_internship(id):
    return 'Hello World!'

@app.route('/internships/student/<student_id>', methods=['GET'])
def get_all_internships(student_id):
    return 'Hello World!'
