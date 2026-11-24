import requests
import urllib3

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

BASE_URL = "https://automationexercise.com"


def test_verify_login():

    payload = {
        "email": "playwrighttest123@gmail.com",
        "password": "Test@123"
    }

    response = requests.post(
        f"{BASE_URL}/api/verifyLogin",
        data=payload,
        verify=False
    )

    assert response.status_code == 200
