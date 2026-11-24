import random

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config import *


def test_register_new_user(page):

    page.goto(BASE_URL)

    home = HomePage(page)

    home.open_signup_login()

    email = f"user{random.randint(1000,9999)}@gmail.com"

    login = LoginPage(page)

    login.signup(
        "Playwright User",
        email
    )

    assert page.locator(
        "text=ENTER ACCOUNT INFORMATION"
    ).is_visible()
