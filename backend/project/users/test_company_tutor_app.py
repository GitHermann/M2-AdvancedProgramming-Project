import json
from app import app


def test_company_tutor_sign_in():
    test_company_tutor = {
        "username": "Test",
        "email": "test@companytutor.efrei.net",
        "password": "test",
        "phone": "0667755877",
        "first_name": "Test",
        "last_name": "Test",
        "company_tutor_id": "2024"
    }

    tester = app.test_client()
    response = tester.post('/users/company-tutor/signin', json=test_company_tutor)
    assert response.status_code == 201



def test_company_tutor_log_in_success():
    tester = app.test_client()
    response = tester.post('/users/company-tutor/login', json={'email': 'test@companytutor.efrei.net', 'password': 'test'})
    assert response.status_code == 200

def test_company_tutor_log_in_fail():
    tester = app.test_client()
    response = tester.post('/users/company-tutor/login', json={'email': 'test@efrei.net', 'password': 'tfefhh'})
    assert response.status_code == 400

def test_get_company_tutor_by_id_success():
    tester = app.test_client()
    response = tester.get('/users/company-tutor/65bfb6c9fad170a15ca0c744')
    assert response.status_code == 200

def test_get_company_tutor_by_id_fail():
    tester = app.test_client()
    response = tester.get('/users/company-tutor/65affeb2eb2708310e6404bf')
    assert response.status_code == 404

def test_get_authenticated_company_tutor_profile_success():
    tester = app.test_client()

    # Log in the user
    login_response = tester.post('/users/company-tutor/login', json={'email': 'test@companytutor.efrei.net', 'password': 'test'})
    assert login_response.status_code == 200

    # Use a context manager to make the request with the logged-in session
    with tester as client:
        with client.session_transaction() as session:
            # Access the session dictionary and set the user ID
            session['user'] = login_response.json['user']['_id']['$oid']

        # Make the request to get the profile
        response = tester.get('/users/company-tutor/profile')
        assert response.status_code == 200

def test_get_authenticated_company_tutor_profile_fail():
    tester = app.test_client()
    response = tester.get('/users/company-tutor/profile')
    assert response.status_code == 401

def test_company_tutor_logout_success():
    tester = app.test_client()
    # Log in the user
    login_response = tester.post('/users/company-tutor/login', json={'email': 'test@companytutor.efrei.net', 'password': 'test'})
    assert login_response.status_code == 200

    # Use a context manager to make the request with the logged-in session
    with tester as client:
        with client.session_transaction() as session:
            # Access the session dictionary and set the user ID
            session['user'] = login_response.json['user']['_id']['$oid']

    response = client.post('/users/company-tutor/logout')
    assert response.status_code == 200

def test_company_tutor_logout_fail():
    tester = app.test_client()
    response = tester.post('/users/company-tutor/logout')
    assert response.status_code == 401  # Assuming not authenticated
    # Add more tests with authenticated user

