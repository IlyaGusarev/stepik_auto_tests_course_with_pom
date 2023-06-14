from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(
            *LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(
            *LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

        password_confirm = self.browser.find_element(
            *LoginPageLocators.PASSWORD_CONFIRM)
        password_confirm.send_keys(password)

        submit_button = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_SUBMIT)
        submit_button.click()
