from app import app


@app.route('/user/admin', methods=['POST'])
def add_user_admin():
    return 'Hello World!'


@app.route('/user/admin/<id>', methods=['GET'])
def get_user_admin(id):
    return 'Hello World!'


@app.route('/user/admin/<id>', methods=['PUT'])
def update_user_admin(id):
    return 'Hello World!'


@app.route('/user/admin/<id>', methods=['DELETE'])
def delete_user_admin(id):
    return 'Hello World!'
