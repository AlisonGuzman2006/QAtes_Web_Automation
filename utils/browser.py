from selenium import webdriver

def get_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
