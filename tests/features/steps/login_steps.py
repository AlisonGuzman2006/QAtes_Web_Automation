from behave import given, when, then
from selenium import webdriver
from main.ui.pages.login_page import LoginPage
import allure

@given('a web browser is at the todoist login page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://app.todoist.com/auth/login")
    context.login_page = LoginPage(context.browser)

@when('a user enters the Todoist username "{username}" and the Todoist password "{password}" and clicks on the Todoist login button')
def step_impl(context, username, password):
    with allure.step(f'Entering username: {username}'):
        context.login_page.enter_username(username)
    with allure.step(f'Entering password'):
        context.login_page.enter_password(password)
    with allure.step('Clicking on login button'):
        context.login_page.click_login_button()

@when('a user provides incorrect Todoist credentials and clicks on the Todoist login button')
def step_impl(context):
    for row in context.table:
        with allure.step(f'Entering username: {row["username"]}'):
            context.login_page.enter_username(row['username'])
        with allure.step('Entering password'):
            context.login_page.enter_password(row['password'])
        with allure.step('Clicking on login button'):
            context.login_page.click_login_button()

@when('a user enters an empty Todoist username and the Todoist password "{password}" and clicks on the Todoist login button')
def step_impl(context, password):
    with allure.step('Entering empty username'):
        context.login_page.enter_username("")
    with allure.step(f'Entering password'):
        context.login_page.enter_password(password)
    with allure.step('Clicking on login button'):
        context.login_page.click_login_button()

@when('a user enters the Todoist username "{username}" and an empty Todoist password and clicks on the Todoist login button')
def step_impl(context, username):
    with allure.step(f'Entering username: {username}'):
        context.login_page.enter_username(username)
    with allure.step('Entering empty password'):
        context.login_page.enter_password("")
    with allure.step('Clicking on login button'):
        context.login_page.click_login_button()

@then('the Todoist url will contain "{expected_url_part}"')
def step_impl(context, expected_url_part):
    with allure.step(f'Checking URL contains: {expected_url_part}'):
        assert expected_url_part in context.browser.current_url

@then('the Todoist error message "{error_message}" is displayed')
def step_impl(context, error_message):
    with allure.step(f'Checking error message: {error_message}'):
        assert context.login_page.get_error_message() == error_message

def after_scenario(context, scenario):
    context.browser.quit()
