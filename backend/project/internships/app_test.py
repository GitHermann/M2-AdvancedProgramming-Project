from app import app

tester = app.test_client()
internship_id = str()


def test_index():
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_add_internship():
    json_data = {
        "title": "stage test api",
        "startDate": [
            2020,
            1,
            1
        ],
        "endDate": [
            2024,
            1,
            1
        ],
        "company": "company B",
        "academicTutor": "academicTutor",
        "companyTutor": "companyTutor"
    }

    response = tester.post("/internship_spaces/65bfa8b4d66a31ac48d56197/internships/65b12927b91ba67d6de2eaad",
                           json=json_data)

    assert response.status_code == 201

    data = response.get_json()
    global internship_id
    internship_id = data['inserted_id']


def test_get_internship():
    response = tester.get("/internship_spaces/65bfa8b4d66a31ac48d56197/internships/" + internship_id)

    assert response.status_code == 200


def test_get_all_internship_in_space():
    response = tester.get("/internship_spaces/65bfa8b4d66a31ac48d56197/internships")

    assert response.status_code == 200


def test_delete_internship():
    response = tester.delete("/internship_spaces/65bfa8b4d66a31ac48d56197/internships/" + internship_id)

    assert response.status_code == 200
