class LoginPage:
    EMAIL_SELECTOR = "element-0"
    PASSWORD_SELECTOR = "element-3"
    LOGIN_BUTTON_SELECTOR = 'button[data-gtm-id="start-email-login"][type="submit"]'

    def __init__(self, driver):
        self.driver = driver

