from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ComponentPages:
    def __init__(self, driver):
        self.driver = driver

    def search_and_fill_by_id(self, id, value):
        field = self.driver.find_element(By.ID, id)
        field.clear()
        field.send_keys(value)

    def click_button_by_css(self, css_selector):
        login_button = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        login_button.click()

    def get_text_by_class_name(self, class_name, timeout=40):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, class_name))
        )
        return element.text

    def get_text_by_class(self, class_selector, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, class_selector))
        )
        return element.text