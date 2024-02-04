from app import app

tester = app.test_client()
internship_space_id = str()

def test_index():
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"

def test_get_internship_space():
    response = tester.get("/internship_spaces/65bfa8b4d66a31ac48d56197")

    assert response.status_code == 200
    

def test_get_all_internship_spaces():
    response  = tester.get("/internship_spaces")

    assert response.status_code == 201

def test_add_internship_space():
    json_data = {
      "name": "Stage de fin d'études test api",
      "promotion": 2024,
      "tutors_instruction": "tutors_instruction",
      "students_instruction": "students_instruction",
      "startSubmissionDate": [
        2024,
        1,
        1
      ],
      "endSubmissionDate": [
        2024,
        6,
        1
      ]
    }

    response = tester.post("/internship_spaces", json= json_data)
    data = response.get_json()

    assert response.status_code == 201
    assert data['message'] == "Intership spaces successfully created"

    global internship_space_id
    internship_space_id = data['inserted_id']

def test_delete_internship_space():
    response = tester.delete("/internship_spaces/"+internship_space_id)

    assert response.status_code == 200

