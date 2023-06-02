# pytest -v -s --tb=line --reruns 2 --language=en test_product_page.py

from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    # time.sleep(99999)
    product_page.product_name_should_be_in_success_message()
    product_page.basket_price_should_match_with_product_price()
