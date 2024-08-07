from selenium.webdriver.common.by import By


def search_and_fill_by_id(context, id, value):
    email_field = context.driver.find_element(By.ID, id)
    email_field.clear()
    email_field.send_keys(value)


def click_button_by_css(context, css_selector):
    login_button = context.driver.find_element(By.CSS_SELECTOR, css_selector)
    login_button.click()
