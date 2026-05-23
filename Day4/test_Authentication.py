import requests
import os
from requests.auth import HTTPDigestAuth

class TestAuthentication:

    def test_Bearer_token_auth(self):
        bearer_token = os.environ.get("FOR_MY_AAPI_REPO")
        request_headers = {"Authorization": f"Bearer {bearer_token}"}
        res = requests.get("https://api.github.com/user/repos", headers=request_headers)
        assert res.status_code == 200, "Wrong Status Code"

    def test_basic_auth(self):
        res = requests.get("https://postman-echo.com/basic-auth", auth=('postman', 'password'))
        assert res.status_code == 200, "Wrong Status Code"
        data = res.json()
        print(data)
        assert data.get("authenticated") is True 

    def test_digest_auth(self):
        res = requests.get("https://postman-echo.com/digest-auth", auth=HTTPDigestAuth('postman', 'password'))
        assert res.status_code == 200, "Wrong Status Code"
        data = res.json()
        print(data)
        assert data.get("authenticated") is True 

    def test_api_key_auth(self):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 55.75,
            "longitude": 37.62,
            "current": "temperature_2m"
        }

        response = requests.get(url, params=params)
        assert response.status_code == 200, "Wrong Status Code"
        data = response.json()

        # Получаем температуру из JSON
        current_temp = data["current"]["temperature_2m"]
        print(f"Текущая температура: {current_temp}°C")


   