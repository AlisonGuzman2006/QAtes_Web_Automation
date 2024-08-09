class LoginPage:
    EMAIL_FIELD_SELECTOR = "element-0"
    PASSWORD_FIELD_SELECTOR = "element-3"
    LOGIN_BUTTON_SELECTOR = 'button[data-gtm-id="start-email-login"][type="submit"]'
    MESSAGE_ERROR_TEXT_SELECTOR = ".a83bd4e0._266d6623._8f5b5f2b.fb8d74bb"

    def __init__(self, driver):
        self.driver = driver
