from core.drivers.chrome_driver import get_chrome_driver
from core.drivers.firefox_driver import get_firefox_driver


def select_browser(browser_name):
    if browser_name == 'chrome':
        return get_chrome_driver()
    elif browser_name == 'firefox':
        return get_firefox_driver()
    else:
        raise ValueError(f"Browser {browser_name} is not supported.")