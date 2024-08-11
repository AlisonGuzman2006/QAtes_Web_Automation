from selenium import webdriver

from core.drivers.options import set_options


def get_firefox_driver():
    options = webdriver.FirefoxOptions()
    set_options(options)
    driver = webdriver.Firefox(options=options)
    return driver
