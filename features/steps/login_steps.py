import time
from behave import given, when, then
from main.ui.component_pages import ComponentPages
from main.ui.login_page import LoginPage


@given('I am logged into Todoist with credentials "{email}" "{password}"')
def step_logged_in_todoist(context,email, password):
    context.component_pages = ComponentPages(context.driver)
    context.login_page = LoginPage(context.driver)
    context.driver.get(context.url)
    context.component_pages.search_and_fill_by_id(context.login_page.EMAIL_SELECTOR, email)
    context.component_pages.search_and_fill_by_id(context.login_page.PASSWORD_SELECTOR, password)
    context.component_pages.click_button_by_css(context.login_page.LOGIN_BUTTON_SELECTOR)


@given('the user is on the Todoist login page')
def step_given_user_on_todoist_login_page(context):
    context.component_pages = ComponentPages(context.driver)
    context.login_page = LoginPage(context.driver)
    context.driver.get(context.url)


@when('the user enters a valid email "{email}"')
def step_when_user_enters_valid_email(context, email):
    context.component_pages.search_and_fill_by_id(context.login_page.EMAIL_SELECTOR, email)


@when('the user enters a valid password "{password}"')
def step_when_user_enters_valid_password(context, password):
    context.component_pages.search_and_fill_by_id(context.login_page.PASSWORD_SELECTOR, password)


@when('the user clicks on the "Log in" button')
def step_when_user_clicks_login_button(context):
    context.component_pages.click_button_by_css(context.login_page.LOGIN_BUTTON_SELECTOR)


@then('the user should be redirected to the Todoist dashboard')
def step_then_user_redirected_to_dashboard(context):
    time.sleep(5)
    expected_url = f"{context.url}/app"
    assert expected_url in context.driver.current_url
