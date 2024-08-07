import time

from behave import given, when, then

from main.ui.login_pages import search_and_fill_by_id, click_button_by_css


@given('the user is on the Todoist login page')
def step_given_user_on_todoist_login_page(context):
    context.driver.get(context.url)
    time.sleep(10)


@when('the user enters a valid email "{email}"')
def step_when_user_enters_valid_email(context, email):
    search_and_fill_by_id(context, "element-0", email)


@when('the user enters a valid password "{password}"')
def step_when_user_enters_valid_password(context, password):
    search_and_fill_by_id(context, "element-3", password)


@when('the user clicks on the "Log in" button')
def step_when_user_clicks_login_button(context):
    click_button_by_css(context, 'button[data-gtm-id="start-email-login"][type="submit"]')


@then('the user should be redirected to the Todoist dashboard')
def step_then_user_redirected_to_dashboard(context):
    time.sleep(2)
    assert f"{context.url}/app" in context.driver.current_url


