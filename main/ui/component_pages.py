from selenium.webdriver.common.by import By


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
