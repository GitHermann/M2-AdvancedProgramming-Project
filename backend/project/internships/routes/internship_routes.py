import json
import bson.json_util as json_util
from flask import request, jsonify

from app import app
from models.internship_model import Internship


@app.route('/internship_spaces/<internship_space_id>/internships/<student_id>', methods=['POST'])
def add_internship(internship_space_id, student_id):
    try:
        data = request.json
        response = Internship.create_internship(data, internship_space_id, student_id)
        return jsonify(response[0]), response[1]
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/internship_spaces/<internship_space_id>/internships/<internship_id>', methods=['GET'])
def get_internship(internship_id, internship_space_id):
    try:
        response = Internship.get_internship(internship_id, internship_space_id)
        return json.loads(json_util.dumps(response[0])), response[1]
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/internships/<internship_id>', methods=['POST'])
def set_internship_status(internship_id):
    try:
        status = request.json['status']
        response = Internship.set_status(internship_id, status)
        return json.loads(json_util.dumps(response[0])), response[1]
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/internship_spaces/<internship_space_id>/internships/<internship_id>', methods=['DELETE'])
def delete_internship(internship_id, internship_space_id):
    try:
        response = Internship.delete_internship(internship_id, internship_space_id)
        return jsonify(response[0]), response[1]
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/internship_spaces/<internship_space_id>/internships', methods=['GET'])
def get_all_internships(internship_space_id):
    try:
        response = Internship.get_all_internships_in_space(internship_space_id)
        return jsonify(response[0]), response[1]
    except Exception as e:
        return jsonify({"error": str(e)}), 500
