from hooks.hooks import create_driver, quit_driver, clean_browser

url = "https://app.todoist.com"
username = "201604530@est.umss.edu",
password = "papasfritas"


def before_all(context):
    context.driver = create_driver(context)
    context.url = url


def after_all(context):
    quit_driver(context.driver)


def before_scenario(context, scenario):
    clean_browser(context)


def after_scenario(context, scenario):
    clean_browser(context)

