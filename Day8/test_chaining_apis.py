import pytest
import requests
import json
import os
from faker import Faker
BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = os.environ.get("GOREST_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
faker = Faker()
class TestChainingAPIs:
    user_id = None
    @pytest.mark.order(1)
    @pytest.mark.dependency(name="create")
    def test_create_user(self):
        data = {
            "name": faker.name(),
            "gender": "male",
            "email": faker.unique.email(),
            "status": "inactive"
        }
        res = requests.post(BASE_URL, json=data, headers=HEADERS)
        assert res.status_code == 201, "wrong status code"
        TestChainingAPIs.user_id = res.json()["id"]
        assert TestChainingAPIs.user_id, "USER_ID is not generated"
        print("\nCREATE Response\n", json.dumps(res.json(), indent=4))
    @pytest.mark.order(2)
    @pytest.mark.dependency(depends=["create"])
    def test_get_user_details(self):
        res = requests.get(f"{BASE_URL}/{TestChainingAPIs.user_id}", headers=HEADERS)
        assert res.status_code == 200, "Get user failed"
        print("\nGET Response:\n", json.dumps(res.json(), indent=4))
    @pytest.mark.order(3)
    @pytest.mark.dependency(depends=["create"])
    def test_update_user(self):
        updated_data = {
            "name": faker.name(),
            "gender": "male",
            "email": faker.unique.email(),
            "status": "inactive"
        }
        res = requests.put(f"{BASE_URL}/{TestChainingAPIs.user_id}", json=updated_data, headers=HEADERS)
        assert res.status_code == 200, "wrong status code"
        print("\nUPDATE Response\n", json.dumps(res.json(), indent=4))
    @pytest.mark.order(4)
    @pytest.mark.dependency(depends=["create"])
    def test_delete_user(self):
        res = requests.delete(f"{BASE_URL}/{TestChainingAPIs.user_id}", headers=HEADERS)
        assert res.status_code == 204, "wrong status code"