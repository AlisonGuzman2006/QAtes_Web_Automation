from selenium import webdriver
import allure
from allure_behave.hooks import allure_report

def before_all(context):
    context.browser = webdriver.Chrome()
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
