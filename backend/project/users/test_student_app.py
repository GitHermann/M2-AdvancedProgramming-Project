import json
from app import app

STUDENT_LOGIN_URL = '/users/student/login'
STUDENT_MAIL = 'test@efrei.net'


def test_student_sign_in():
    test_student = {
        "username": "Test",
        "first_name": "Test",
        "last_name": "Test",
        "email": "test@efrei.net",
        "password": "test",
        "phone": "0667755587",
        "student_id": "test",
        "promotion": "2024"
    }

    tester = app.test_client()
    response = tester.post('/users/student/signin', json=test_student)
    assert response.status_code == 201


def test_student_log_in_success():
    tester = app.test_client()
    response = tester.post(STUDENT_LOGIN_URL, json={'email': STUDENT_MAIL, 'password': 'test'})
    assert response.status_code == 200


def test_student_log_in_fail():
    tester = app.test_client()
    response = tester.post(STUDENT_LOGIN_URL, json={'email': STUDENT_MAIL, 'password': 'tfefhh'})
    assert response.status_code == 400


def test_get_student_by_id_success():
    tester = app.test_client()
    response = tester.get('/users/student/65affeb2eb2708310e6404bd')
    assert response.status_code == 200


def test_get_student_by_id_fail():
    tester = app.test_client()
    response = tester.get('/users/student/65affeb2eb2708310e6404bf')
    assert response.status_code == 404


def test_get_authenticated_student_profile_success():
    tester = app.test_client()

    # Log in the user
    login_response = tester.post(STUDENT_LOGIN_URL, json={'email': STUDENT_MAIL, 'password': 'test'})
    assert login_response.status_code == 200

    # Use a context manager to make the request with the logged-in session
    with tester as client:
        with client.session_transaction() as session:
            # Access the session dictionary and set the user ID
            session['user'] = login_response.json['user']['_id']['$oid']

        # Make the request to get the profile
        response = tester.get('/users/student/profile')
        assert response.status_code == 200


def test_get_authenticated_student_profile_fail():
    tester = app.test_client()
    response = tester.get('/users/student/profile')
    assert response.status_code == 401


def test_student_logout_success():
    tester = app.test_client()
    # Log in the user
    login_response = tester.post(STUDENT_LOGIN_URL, json={'email': STUDENT_MAIL, 'password': 'test'})
    assert login_response.status_code == 200

    # Use a context manager to make the request with the logged-in session
    with tester as client:
        with client.session_transaction() as session:
            # Access the session dictionary and set the user ID
            session['user'] = login_response.json['user']['_id']['$oid']

    response = client.post('/users/student/logout')
    assert response.status_code == 200


def test_student_logout_fail():
    tester = app.test_client()
    response = tester.post('/users/student/logout')
    assert response.status_code == 401  # Assuming not authenticated
    # Add more tests with authenticated user
