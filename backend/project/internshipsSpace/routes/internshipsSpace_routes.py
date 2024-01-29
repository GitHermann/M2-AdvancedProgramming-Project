import json
import bson.json_util as json_util
from flask import request, jsonify

from app import app
from models.internshipsSpace_model import InternshipsSpace

@app.route('/internships_space', methods=['POST'])
def add_internships_space():
  try:
    data = request.json
    response = InternshipsSpace.createIntershipsSpace(data)
    return jsonify(response[0]), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@app.route('/internships_space', methods=['GET'])
def get_all_internships_space():
  try:
    response = InternshipsSpace.getAllInternshipsSpace()
    return json.loads(json_util.dumps(response[0])), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@app.route('/internships_space/<id>', methods=['GET'])
def get_internships_space(id):
  try:
    response = InternshipsSpace.getInternshipsSpace(id)
    return json.loads(json_util.dumps(response[0])), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@app.route('/internships_space/<id>', methods=['POST'])
def edit_internships_space(id):
  try:
    data = request.json
    response = InternshipsSpace.editInternshipsSpace(id, data)
    return jsonify(response[0]), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@app.route('/internships_space/<id>', methods=['DELETE'])
def delete_internships_space(id):
  try:
    response = InternshipsSpace.deleteInternshipsSpace(id)
    return jsonify(response[0]), response[1]
  except Exception as e:
    return jsonify({'error': str(e)}), 500