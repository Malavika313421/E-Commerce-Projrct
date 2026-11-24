import requests
import urllib3

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

BASE_URL = "https://automationexercise.com"

def test_get_brands():

    response = requests.get(
        f"{BASE_URL}/api/brandsList",
        verify=False
    )

    assert response.status_code == 200
