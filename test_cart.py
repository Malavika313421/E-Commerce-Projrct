from pages.products_page import ProductsPage
from pages.cart_page import CartPage

BASE_URL = "https://automationexercise.com"


def test_add_product_to_cart(page):

    page.goto(BASE_URL)

    page.click("a[href='/products']")

    product = ProductsPage(page)

    product.add_first_product_to_cart()

    page.click("text=View Cart")

    cart = CartPage(page)

    assert cart.verify_cart()


def test_remove_product_from_cart(page):

    page.goto(BASE_URL)

    page.click("a[href='/products']")

    product = ProductsPage(page)

    product.add_first_product_to_cart()

    page.click("text=View Cart")

    cart = CartPage(page)

    cart.remove_product()
