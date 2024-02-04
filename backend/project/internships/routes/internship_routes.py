import json
import bson.json_util as json_util
from flask import request, jsonify

from app import app
from models.internship_model import Internship

@app.route('/internship_spaces/<internship_space_id>/internships', methods=['POST'])
def add_internship(internship_space_id):
    try:
        data = request.json
        response = Internship.createInternship(data, internship_space_id)
        return jsonify(response[0]), response[1]
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/internship_spaces/<internship_space_id>/internships/<id>', methods=['GET'])
def get_internship(id, internship_space_id):
    try:
        response = Internship.getInternship(id, internship_space_id)
        return json.loads(json_util.dumps(response[0])), response[1]
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/internships/<id>', methods=['PUT'])
def update_internship(id):
    return 'Hello World!'

@app.route('/internships/<id>', methods=['DELETE'])
def delete_internship(id):
    return 'Hello World!'

@app.route('/internships/student/<student_id>', methods=['GET'])
def get_all_internships(student_id):
    return 'Hello World!'
