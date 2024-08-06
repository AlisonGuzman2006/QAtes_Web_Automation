from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def enter_username(self, username):
        email_field = self.browser.find_element(By.ID, 'element-0')
        email_field.clear()
        email_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.browser.find_element(By.ID, 'element-3')
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.browser.find_element(By.CSS_SELECTOR, '.rWfXb_e')
        login_button.click()

    def get_error_message(self):
        error_element = self.browser.find_element(By.CSS_SELECTOR, '.a83bd4e0._266d6623._8f5b5f2b.fb8d74bb')
        return error_element.text
