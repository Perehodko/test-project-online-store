from .locators import MainPageLocators
from .base_page import BasePage

class CartPage(BasePage):
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*MainPageLocators.BASKET_EMPTY_MESSAGE), "Message about empty basket isn't present"

