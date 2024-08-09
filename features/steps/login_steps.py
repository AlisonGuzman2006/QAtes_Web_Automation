import time
from behave import given, when, then
from main.ui.component_pages import ComponentPages
from main.ui.login_page import LoginPage

@given('the user is on the Todoist login page')
def step_given_user_on_todoist_login_page(context):
    context.component_pages = ComponentPages(context.driver)
    context.login_page = LoginPage(context.driver)
    context.driver.get(context.url)
    # No es necesario usar time.sleep(10) porque las esperas explícitas ya están en ComponentPages

@when('the user enters a valid email "{email}"')
def step_when_user_enters_valid_email(context, email):
    context.component_pages.search_and_fill_by_id(context.login_page.EMAIL_FIELD_SELECTOR, email)

@when('the user enters a valid password "{password}"')
def step_when_user_enters_valid_password(context, password):
    context.component_pages.search_and_fill_by_id(context.login_page.PASSWORD_FIELD_SELECTOR, password)

@when('the user clicks on the "Log in" button')
def step_when_user_clicks_login_button(context):
    context.component_pages.click_button_by_css(context.login_page.LOGIN_BUTTON_SELECTOR)

@then('the user should be redirected to the Todoist dashboard')
def step_then_user_redirected_to_dashboard(context):
    # No se necesita time.sleep(10) ya que la espera está manejada por WebDriverWait en click_button_by_css
    assert f"{context.url}/app" in context.driver.current_url

# Scenario: Unsuccessful login with invalid credentials

@when('the user enters an invalid email "{invalid_email}"')
def step_when_user_enters_invalid_email(context, invalid_email):
    context.component_pages.search_and_fill_by_id(context.login_page.EMAIL_FIELD_SELECTOR, invalid_email)

@when('the user enters an invalid password "{invalid_password}"')
def step_when_user_enters_invalid_password(context, invalid_password):
    context.component_pages.search_and_fill_by_id(context.login_page.PASSWORD_FIELD_SELECTOR, invalid_password)

@then('the Todoist error message "{expected_message}" is displayed')
def step_the_todoist_error_message_is_displayed(context, expected_message):
    actual_message = context.component_pages.get_text_by_class(context.login_page.MESSAGE_ERROR_TEXT_SELECTOR)
    assert actual_message == expected_message, f"Expected '{expected_message}', but got '{actual_message}'"
