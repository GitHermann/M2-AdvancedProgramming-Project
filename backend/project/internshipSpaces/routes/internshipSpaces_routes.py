import json
import bson.json_util as json_util
from flask import request, jsonify

from app import app
from models.internshipSpaces_model import InternshipSpaces


@app.route('/internship_spaces', methods=['POST'])
def add_internship_spaces():
    try:
        data = request.json
        response = InternshipSpaces.create_internship_spaces(data)
        return jsonify(response[0]), response[1]
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/internship_spaces', methods=['GET'])
def get_all_internship_spaces():
    try:
        response = InternshipSpaces.get_all_internship_spaces()
        return json.loads(json_util.dumps(response[0])), response[1]
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/internship_spaces/<internship_space_id>', methods=['GET'])
def get_internship_spaces(internship_space_id):
    try:
        response = InternshipSpaces.get_internship_spaces(internship_space_id)
        return json.loads(json_util.dumps(response[0])), response[1]
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/internship_spaces/<internship_space_id>', methods=['PUT'])
def edit_internship_spaces(internship_space_id):
    try:
        data = request.json
        response = InternshipSpaces.edit_internship_spaces(internship_space_id, data)
        return jsonify(response[0]), response[1]
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/internship_spaces/<internship_space_id>', methods=['DELETE'])
def delete_internship_spaces(internship_space_id):
    try:
        response = InternshipSpaces.delete_internship_spaces(internship_space_id)
        return jsonify(response[0]), response[1]
    except Exception as e:
        return jsonify({'error': str(e)}), 500
