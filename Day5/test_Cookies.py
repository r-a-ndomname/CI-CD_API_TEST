import requests 


class TestCookies:
    def test_cookies_in_response(self):
        url = "https://www.google.com/"
        res = requests.get(url)
        assert res.status_code == 200,'Wrong status code'
        all_cookies = res.cookies
        print("All cookies : ", all_cookies)

        # Assert Cookie and check if it is not none
        assert "AEC" in all_cookies, "AEC not found"
        assert all_cookies.get("AEC") is not None, "AEC is None"

        cookie_value = all_cookies.get("AEC")
        print("Cookie value : ",cookie_value)
        for key, value in all_cookies.items():
            print(f"{key}: {value}")