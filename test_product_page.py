# pytest -v -s --tb=line --reruns 2 --language=en test_product_page.py

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_name_should_be_in_success_message()
    product_page.basket_price_should_match_with_product_price()
