import json

from flask import request, jsonify
import bson.json_util as json_util
from internship_report.models.internship_report_model import InternshipReport
from app import app, session


@app.route('/documents/internship-report/upload', methods=['POST'])
def upload_internship_report():
    try:
        data_body = {
            'internship': request.form.get('internship'),
            'document_name': request.files.get('file').filename,
            'level_of_confidentiality': request.form.get('level_of_confidentiality')
        }

        file_data = request.files.get('file')
        if not file_data:
            return jsonify({"error": "No file provided"}), 400

        document_instance = InternshipReport(data_body, file_data)
        response = document_instance.create_document(data_body, file_data)

        return jsonify(response), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/documents/internship-report/download/<file_id>', methods=['GET'])
def download_internship_report(file_id):
    data_body = {
        'internship': None,
        'document_name': None,
        'level_of_confidentiality': None
    }
    file_data = None
    document_instance = InternshipReport(data_body, file_data)
    return document_instance.get_document(file_id)
