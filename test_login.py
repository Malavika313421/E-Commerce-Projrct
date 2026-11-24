from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import BASE_URL, EMAIL, PASSWORD


def test_login(page):
    page.goto(
        BASE_URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    home = HomePage(page)
    home.open_signup_login()

    login = LoginPage(page)
    login.login(
        EMAIL,
        PASSWORD
    )

    assert page.locator(
        "text=Logged in as"
    ).is_visible()
