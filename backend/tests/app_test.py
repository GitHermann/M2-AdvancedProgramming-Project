import os
from project.app import app

def test_init():

  ROOT_DIR = os.path.abspath(os.curdir)
  print(ROOT_DIR)

"""



def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"
    """