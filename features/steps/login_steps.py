from behave import given, when, then
from selenium import webdriver


@given('the user is on the Todoist login page')
def step_given_user_on_todoist_login_page(context):
    context.browser = webdriver.Chrome()  # Ensure you have the correct WebDriver for your browser
    context.browser.get("https://todoist.com/users/showlogin")


@when('the user enters a valid email "{email}"')
def step_when_user_enters_valid_email(context, email):
    #email_field = context.browser.find_element_by_id("email")  # Ensure the correct selector is used
    #email_field.send_keys(email)
    print("Hola")


@when('the user enters a valid password "{password}"')
def step_when_user_enters_valid_password(context, password):
    #password_field = context.browser.find_element_by_id("password")  # Ensure the correct selector is used
    #password_field.send_keys(password)
    print("Hola")


@when('the user clicks on the "Log in" button')
def step_when_user_clicks_login_button(context):
    #login_button = context.browser.find_element_by_css_selector(".submit_btn")  # Ensure the correct selector is used
    #login_button.click()
    print("Hola")


@then('the user should be redirected to the Todoist dashboard')
def step_then_user_redirected_to_dashboard(context):
    # Ensure the correct URL or page element to verify successful login
    #assert "app.todoist.com" in context.browser.current_url
    print("Hola")


@then('the user should see a welcome message "Welcome back!"')
def step_then_user_sees_welcome_message(context):
    #welcome_message = context.browser.find_element_by_css_selector(".welcome_message")  # Ensure the correct selector is used
    #assert welcome_message.text == "Welcome back!"
    print("Hola")


# Clean up after the scenario
def after_scenario(context, scenario):
    context.browser.quit()
