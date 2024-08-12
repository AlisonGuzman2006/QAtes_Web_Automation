from core.ui.select_browser import select_browser


def create_driver(context):
    browser = context.config.userdata.get("browser", "chrome")
    return select_browser(browser)


def quit_driver(driver):
    if driver:
        driver.quit()
