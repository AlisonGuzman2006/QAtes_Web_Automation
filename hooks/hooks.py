from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def create_driver():
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    return driver


def quit_driver(driver):
    if driver:
        driver.quit()
