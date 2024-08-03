from .base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def enter_username(self, username):
        email_input = self.find_element(*LoginLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.find_element(*LoginLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        self.click_element(*LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(*LoginLocators.ERROR_MESSAGE).text
