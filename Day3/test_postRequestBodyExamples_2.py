import requests 
import json 
import pytest
from dataclasses import dataclass

student_id = None #Global variable
BASE_URL = "http://localhost:3000/students"
request_headers = {"Content-Type": "application/json"}

def test_createStudentUsingExternalFile():
    global student_id
    @dataclass
    class Student:
        name: str
        location:str
        phone:str
        courses:list

    student = Student("Supriti", "Japan", "12469", ["Python", "Java"])
    request_body = student.__dict__
    response = requests.post(BASE_URL, json=request_body)

    assert response.status_code == 201, "Status code is not 201"
    response_body = response.json()
    assert response_body["name"] == "Supriti", "Name is not correct"
    assert response_body["location"] == "Japan", "Location is not correct"
    assert response_body["phone"] == "12469", "Phone is not correct"
    assert response_body["courses"][0] == "Python", "Course 1 should be Python"
    assert response_body["courses"][1] == "Java", "Course 2 should be Java"
    student_id = response_body["id"]
    print(response.json())


@pytest.fixture(autouse=True)
def delete_student():
    yield
    response = requests.delete(f"{BASE_URL}/{student_id}")
    assert response.status_code == 200, "Wrong Status code"
    print(response.json())
    print("Student Deleted")