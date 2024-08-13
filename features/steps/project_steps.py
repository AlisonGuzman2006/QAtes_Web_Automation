import time


from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from main.ui.project_page import ProjectPage
from main.ui.todoist_today_page import TodoistTodayPage
from main.ui.component_pages import ComponentPages

@given('the user is in the team dashboard')
def step_given_user_on_team_dashboard(context):
    context.component_pages = ComponentPages(context.driver)
    context.today_dashboard = TodoistTodayPage(context.component_pages)
    context.project_dashboard = ProjectPage(context.driver)
    context.component_pages.click_button_by_css(context.project_dashboard.PROJECT_DASHBOARD_SELECTOR)
    time.sleep(3)

@given('the user creates a new project "{Project}"')
def step_given_user_create_a_new_project(context, Project):
    context.component_pages.click_button_by_css(context.project_dashboard.ADD_ELEMENT_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.project_dashboard.ADD_PROJECT_BUTTON_SELECTOR)
    time.sleep(3)
    context.component_pages.search_and_fill_by_id(context.project_dashboard.NAME_PROJECT_SELECTOR, Project)
    context.component_pages.click_button_by_css(context.project_dashboard.CREATE_PROJECT_BUTTON_SELECTOR)
    time.sleep(3)

@when('the user sees the options of a project')
def step_when_user_sees_project_options(context):
    context.component_pages.click_button_by_css(context.project_dashboard.VIEW_OPTION_PROJECT_SELECTOR)
    time.sleep(3)

@then('the user duplicates the selected active project')# observacion no esta ejecutando desde aqui
def step_when_user_duplicates_selected_project(context):
    context.component_pages.click_button_by_css(context.project_dashboard.DUPLICATE_PROJECT_OPTION_SELECTOR)
    context.component_pages.click_button_by_css(context.project_dashboard.PROJECT_DASHBOARD_SELECTOR_2)
    time.sleep(3)


@then('the user should see the duplicate of the project "Copy of {Project}" in the list projects of the Team')
def step_then_user_sees_the_duplicate_project(context, Project):
    project_name = f"Copy of {Project}"
    list_of_projects = context.project_dashboard.get_list_of_projects()
    assert project_name in list_of_projects, f"Expected project '{project_name}' not found in the project list."
    time.sleep(3)

#esta por verse si funciona

@when('the user creates a new folder "{folder}"')
def step_when_user_creates_new_folder(context, folder):
    context.component_pages.click_button_by_css(context.project_dashboard.VIEW_OPTION_PROJECT_SELECTOR)
    time.sleep(3)
    context.component_pages.click_button_by_css(context.project_dashboard.OPTION_ORGANIZE_INTO_THE_FOLDER_SELECTOR)
    time.sleep(3)
    context.component_pages.click_button_by_css(context.project_dashboard.CREATE_FOLDER_OPTION_SELECTOR)
    '''context.component_pages.click_button_by_css(context.project_dashboard.PROJECT_DASHBOARD_SELECTOR_2)
    context.component_pages.click_button_by_css(context.project_dashboard.ADD_ELEMENT_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.project_dashboard.ADD_FOLDER_BUTTON_SELECTOR)'''
    time.sleep(3)
    context.component_pages.search_and_fill_by_css(context.project_dashboard.NAME_FOLDER_SELECTOR, folder)
    time.sleep(3)

@when('the user adds the created project to the new folder')
def step_when_user_add_project_to_folder(context):
    '''context.component_pages.click_button_by_css(context.project_dashboard.SELECT_PROJECT_SELECTOR)
    time.sleep(3)
    context.component_pages.click_button_by_css(context.project_dashboard.SELECT_CHECK_PROJECT_SELECTOR)'''
    context.component_pages.click_button_by_css(context.project_dashboard.CREATE_FOLDER_BUTTON_SELECTOR)
    time.sleep(3)

@then('the user should see a pop-up message "Folder “project” has been created"')
def step_then_user_see_confirmation_to_folder_created(context, Project):
    time.sleep(3)
    is_message_present = context.project_dashboard.is_folder_created_message_present(Project)
    assert is_message_present, f"Expected pop-up message 'Folder {Project} has been created' not found."
    time.sleep(3)
