from project.app import app

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")
    print(app.config['MONGO_URI'])

    assert response.status_code == 200
    assert response.data == b"Hello, World!"