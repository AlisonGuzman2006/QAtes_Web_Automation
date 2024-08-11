from selenium import webdriver

from core.drivers.options import set_options


def get_chrome_driver():
    options = webdriver.ChromeOptions()
    set_options(options)
    driver = webdriver.Chrome(options=options)
    return driver
