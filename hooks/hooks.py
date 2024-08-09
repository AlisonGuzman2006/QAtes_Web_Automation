from selenium.webdriver.chrome import webdriver

from core.ui.select_browser import select_browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



def create_driver(context):
    browser = context.config.userdata.get("browser", "chrome")
    return select_browser(browser)


def quit_driver(driver):
    if driver:
        driver.quit()
