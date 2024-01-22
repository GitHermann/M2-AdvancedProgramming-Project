from project.app import app


@app.route('/internships', methods=['POST'])
def add_internship():
    return 'Hello World!'


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
