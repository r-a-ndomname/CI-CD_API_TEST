import requests, json, os

BASE_URL = "http://gorest.co.in/public/v2/users"
TOKEN = os.environ.get("GOREST_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

class TestGetUser:
    def test_get_user(self, create_user):
        user_id = create_user
        assert user_id is not None, "User ID not set by create user test"
        response = requests.get(url=f"{BASE_URL}/{user_id}", headers=HEADERS)
        assert response.status_code == 200, "User fetch failed"
        print("\nGET Response:\n", json.dumps(response.json(), indent=4))
        assert response.json()["id"] == user_id