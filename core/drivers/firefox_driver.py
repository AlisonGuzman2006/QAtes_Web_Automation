from selenium import webdriver


def get_firefox_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Firefox(options=options)
    return driver
