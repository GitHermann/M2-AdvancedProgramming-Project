import json

from flask import request, jsonify
import bson.json_util as json_util

from student.models.student_model import Student
from app import app, session


@app.route('/documents/', methods=['POST'])
def add_document():
    try:
        data = request.json
        InternshipReport = InternshipReport(data)
        response = student_instance.create_student(data)
        return jsonify({"message": str(response)}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

