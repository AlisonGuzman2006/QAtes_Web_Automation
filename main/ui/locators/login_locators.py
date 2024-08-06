from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.ID, 'element-0')
    PASSWORD_INPUT = (By.ID, 'element-3')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.rWfXb_e')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.a83bd4e0._266d6623._8f5b5f2b.fb8d74bb')
