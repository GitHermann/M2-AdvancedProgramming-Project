import json
import bson.json_util as json_util
from flask import request, jsonify

from app import app
from models.internshipSpaces_model import InternshipSpaces

@app.route('/internship_spaces', methods=['POST'])
def add_internship_spaces():
  try:
    data = request.json
    response = InternshipSpaces.createIntershipSpaces(data)
    return jsonify(response[0]), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@app.route('/internship_spaces', methods=['GET'])
def get_all_internship_spaces():
  try:
    response = InternshipSpaces.getAllInternshipSpaces()
    return json.loads(json_util.dumps(response[0])), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@app.route('/internship_spaces/<id>', methods=['GET'])
def get_internship_spaces(id):
  try:
    response = InternshipSpaces.getInternshipSpaces(id)
    return json.loads(json_util.dumps(response[0])), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@app.route('/internship_spaces/<id>', methods=['PUT'])
def edit_internship_spaces(id):
  try:
    data = request.json
    response = InternshipSpaces.editInternshipSpaces(id, data)
    return jsonify(response[0]), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@app.route('/internship_spaces/<id>', methods=['DELETE'])
def delete_internship_spaces(id):
  try:
    response = InternshipSpaces.deleteInternshipSpaces(id)
    return jsonify(response[0]), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500