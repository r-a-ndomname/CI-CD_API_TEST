import requests 
import json 
import pytest

student_id = None #Global variable
BASE_URL = "http://localhost:3000/students"
request_headers = {"Content-Type": "application/json"}

def test_createStudentUsingDictionary():
    global student_id
    request_body = {
        "name": "Scott",
        "location": "France",
        "phone": "123456",
        "courses": ["C", "C++"]
    }

    response = requests.post(BASE_URL, data=json.dumps(request_body), headers=request_headers)
    assert response.status_code == 201, "Status code is not 201"
    response_body = response.json()
    assert response_body["name"] == "Scott", "Name is not correct"
    assert response_body["location"] == "France", "Location is not correct"
    assert response_body["phone"] == "123456", "Phone is not correct"
    assert response_body["courses"][0] == "C", "Course 1 should be C"
    assert response_body["courses"][1] == "C++", "Course 2 should be C++"
    student_id = response_body["id"]
    print(response.json())

@pytest.fixture(autouse=True)
def delete_student():
    yield 
    response = requests.delete(f"{BASE_URL}/{student_id}")
    assert response.status_code == 200
    print("student deleted")