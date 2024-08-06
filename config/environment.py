import os
from selenium import webdriver
from allure_behave.hooks import allure_report


def before_all(context):
    browser = os.getenv('BROWSER', 'chrome')
    if browser == 'chrome':
        context.browser = webdriver.Chrome()
    elif browser == 'edge':
        context.browser = webdriver.Edge()
    else:
        raise ValueError(f"Browser '{browser}' is not supported")

    context.browser.implicitly_wait(10)
    allure_report.before_all(context)


def before_scenario(context, scenario):
    context.browser.delete_all_cookies()
    allure_report.before_scenario(context, scenario)


def after_scenario(context, scenario):
    context.browser.quit()
    allure_report.after_scenario(context, scenario)


def after_all(context):
    allure_report.after_all(context)
