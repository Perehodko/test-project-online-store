from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        CORRECT_LOGIN_RULE = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        assert  CORRECT_LOGIN_RULE  == self.browser.current_url, "URL is not correct" #переписать эту проверку на вхождение login в URL

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password = "12abc345cdf"):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
