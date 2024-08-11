import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ComponentPages:
    def __init__(self, driver):
        self.driver = driver

    def search_and_fill_by_id(self, id, value):
        field = self.driver.find_element(By.ID, id)
        field.clear()
        field.send_keys(value)

    def search_and_fill_by_css_selector(self, css_selector, value):
        field = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        field.clear()
        field.send_keys(value)

    def click_button_by_css(self, css_selector):
        login_button = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        login_button.click()
        return login_button

    def get_element_by_css(self, css_selector, timeout=1):
        #wait = WebDriverWait(self.driver, timeout)
        #time.sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        return element

    def get_elements_by_css(self, css_selector):
        elements = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
        return elements



