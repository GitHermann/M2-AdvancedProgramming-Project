from project.app import app


@app.route('/user/tutorAcademic', methods=['POST'])
def add_user_tutor_academic():
    return 'Hello World!'


@app.route('/user/tutorAcademic/<id>', methods=['GET'])
def get_user_tutor_academic(id):
    return 'Hello World!'


@app.route('/user/tutorAcademic/<id>', methods=['PUT'])
def update_user_tutor_academic(id):
    return 'Hello World!'


@app.route('/user/tutorAcademic/<id>', methods=['DELETE'])
def delete_user_tutor_academic(id):
    return 'Hello World!'
