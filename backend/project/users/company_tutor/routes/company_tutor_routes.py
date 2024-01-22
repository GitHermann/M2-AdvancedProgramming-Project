from project.app import app


@app.route('/user/tutorEntreprise', methods=['POST'])
def add_user_tutor_entreprise():
    return 'Hello World!'


@app.route('/user/tutorEntreprise/<id>', methods=['GET'])
def get_user_tutor_entreprise(id):
    return 'Hello World!'


@app.route('/user/tutorEntreprise/<id>', methods=['PUT'])
def update_user_tutor_entreprise(id):
    return 'Hello World!'


@app.route('/user/tutorEntreprise/<id>', methods=['DELETE'])
def delete_user_tutor_entreprise(id):
    return 'Hello World!'
