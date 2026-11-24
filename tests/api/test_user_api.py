import requests
import urllib3

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

BASE_URL = "https://automationexercise.com"


def test_search_product():

    payload = {
        "search_product": "Top"
    }

    response = requests.post(
        f"{BASE_URL}/api/searchProduct",
        data=payload,
        verify=False
    )

    assert response.status_code == 200

    print(response.json())
