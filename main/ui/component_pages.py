from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ComponentPages:
    EXPLICIT_TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    def search_and_fill_by_id(self, id, value):
        field = WebDriverWait(self.driver, self.EXPLICIT_TIMEOUT).until(
            EC.visibility_of_element_located((By.ID, id))
        )
        field.clear()
        field.send_keys(value)

    def click_button_by_css(self, css_selector):
        button = WebDriverWait(self.driver, self.EXPLICIT_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        button.click()

    def search_and_fill_by_css(self, css_selector, value):
        field = WebDriverWait(self.driver, self.EXPLICIT_TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        field.send_keys(value)

    def get_text_by_class(self, class_selector):
        field = WebDriverWait(self.driver, self.EXPLICIT_TIMEOUT).until(
            EC.visibility_of_element_located((By.CLASS_NAME, class_selector))
        )
        return field.text

    def get_elements_by_class(self, class_selector):
        fields = WebDriverWait(self.driver, self.EXPLICIT_TIMEOUT).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, class_selector))
        )
        return fields

    def wait_url(self, expected_url):
        WebDriverWait(self.driver, self.EXPLICIT_TIMEOUT).until(
            EC.url_to_be(expected_url)
        )

    def get_text_by_css_selector(self, css_selector):
        field = WebDriverWait(self.driver, self.EXPLICIT_TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return field.text
