from project.app import app


@app.route('/user/student', methods=['POST'])
def add_user_student():
    return 'Hello World!'


@app.route('/user/student/<id>', methods=['GET'])
def get_user_student(id):
    return 'Hello World!'


@app.route('/user/student/<id>', methods=['PUT'])
def update_user_student(id):
    return 'Hello World!'


@app.route('/user/student/<id>', methods=['DELETE'])
def delete_user_student(id):
    return 'Hello World!'
