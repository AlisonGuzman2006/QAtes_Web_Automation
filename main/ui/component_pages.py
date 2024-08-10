from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class ComponentPages:
    def __init__(self, driver):
        self.driver = driver

    def search_and_fill_by_id(self, id, value):
        # Aseguramos que el elemento esté visible antes de interactuar con él.
        field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, id))
        )
        field.clear()
        field.send_keys(value)

    def click_button_by_css(self, css_selector):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        login_button.click()

    def get_text_by_class(self, class_selector, timeout=10):
        message_error = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, class_selector))
        )
        return message_error.text

    def wait_for_url_contains(self, substring, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(substring))
        return substring in self.driver.current_url


