from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ITEM_IN_BASKET)

    def message_basket_is_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE)
