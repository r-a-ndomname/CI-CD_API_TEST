import pytest
import json
import requests
import os
from faker import Faker

BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = os.environ.get("GOREST_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

@pytest.fixture(scope="session", autouse=True)
def create_user():
    faker = Faker()
    data = {
        "name": faker.name(),
        "gender": "male",
        "email": faker.unique.email(),
        "status": "inactive"
    }
    response = requests.post(BASE_URL, json=data, headers=HEADERS)
    assert response.status_code == 201, "Create user failed"
    print("\nCREATE Response:\n", json.dumps(response.json(), indent=4))
    return response.json()["id"]