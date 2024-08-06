from QAtes_Web_Automation.hooks.hooks import create_driver, quit_driver


url = "https://app.todoist.com"
username = "201604530@est.umss.edu",
password = "1234567890Abc"


def before_all(context):
    context.driver = create_driver()


def after_all(context):
    quit_driver(context.driver)
