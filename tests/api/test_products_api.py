from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.config import BASE_URL


def test_search_product(page):

    page.goto(
        BASE_URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    home = HomePage(page)

    home.open_products()

    product = ProductsPage(page)

    product.search_product("Top")

    assert page.locator(
        "text=Searched Products"
    ).is_visible()
