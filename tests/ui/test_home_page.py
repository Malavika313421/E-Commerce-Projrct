from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config import *

BASE_URL = "https://automationexercise.com"


def test_home_page(page):

    page.goto(BASE_URL)

    home = HomePage(page)

    assert page.title() != ""
