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
        assert product_name == message, 'Product name not in message'

    def basket_price_should_match_with_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE).text
        assert product_price in basket_price, 'Basket price don\'t match with product price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE),\
            'success message should not appear'

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE),\
            'Success message not disappear'
