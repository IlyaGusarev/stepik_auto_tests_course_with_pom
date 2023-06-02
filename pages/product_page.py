from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def product_name_should_be_in_success_message(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_IN_MESSAGE).text
        assert product_name == message

    def basket_price_should_match_with_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE).text
        assert product_price in basket_price