# pytest -v -s --tb=line --language=en test_product_page.py

import time
import string
import random
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


# pytest -v -s --tb=line --language=en test_product_page.py::TestUserAddToBasketFromProductPage
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link_product_page):
        email = ''.join(
            [random.choice(string.ascii_letters) for _ in range(5)]
        ) + '@fakemail.com'
        password = ''.join(
            [random.choice(
                string.ascii_letters + string.digits + string.punctuation
            ) for n in range(10)])

        login_page = LoginPage(browser, link_product_page)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link_product_page):
        product_page = ProductPage(browser, link_product_page)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, link_product_page):
        product_page = ProductPage(browser, link_product_page)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.product_name_should_be_in_success_message()
        product_page.basket_price_should_match_with_product_price() 


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail
    ),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_name_should_be_in_success_message()
    product_page.basket_price_should_match_with_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(
    browser, link_product_page
):
    product_page = ProductPage(browser, link_product_page)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, link_product_page):
    product_page = ProductPage(browser, link_product_page)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(
    browser, link_product_page
):
    product_page = ProductPage(browser, link_product_page)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(
    browser,
    link_for_test_login_on_product_page
):
    page = ProductPage(browser, link_for_test_login_on_product_page)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(
    browser,
    link_for_test_login_on_product_page
):
    page = ProductPage(browser, link_for_test_login_on_product_page)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(
    browser, link_product_page
):
    page = ProductPage(browser, link_product_page)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.message_basket_is_empty()
