import time
from behave import given, when, then

from selenium.webdriver import Keys

from main.ui.inbox_dashboard_page import InboxDashboardPage
from main.ui.new_task_page import NewTaskPage
from main.ui.todoist_today_page import TodoistTodayPage
from main.ui.component_pages import ComponentPages
from main.ui.view_panel_page import ViewPanelPage

from core.assertions.content_assertions import assert_is_text_contained_elements, assert_element_is_deleted

@given('the user is in the Today page dashboard for task management')
def step_given_user_in_today_dashboard_task_management(context):
    context.component_pages = ComponentPages(context.driver)
    context.today_dashboard = TodoistTodayPage(context.driver)
    context.new_task = NewTaskPage(context.driver)
    context.view_panel = ViewPanelPage(context.driver)
    context.driver.get(context.today_dashboard.TODAY_DASHBOARD_URL)
    time.sleep(3)

@when('the user creates a new task with title "{task_title}"')
def step_when_user_creates_new_task(context, task_title):
    context.component_pages.click_button_by_css(context.today_dashboard.ADD_TASK_BUTTON_DASHBOARD_SELECTOR)
    time.sleep(1)
    context.component_pages.search_and_fill_by_css_selector(context.new_task.NAME_TASK_FIELD_SELECTOR, task_title)
    time.sleep(1)
    context.component_pages.click_button_by_css(context.new_task.ADD_TASK_BUTTON_FORM_SELECTOR)
    time.sleep(3)


@when('the user edits the task with new title')
def step_when_user_edits_task(context):
    context.today_dashboard = TodoistTodayPage(context.driver)
    context.today_dashboard.edit_task()

@when('the user deletes the task')
def step_when_user_deletes_task(context):
    context.today_dashboard.delete_task_management("New Title")
    time.sleep(3)

@then('the task "{task_name}" should no longer appear in the task list')
def step_impl(context, task_name):
    task_list = context.today_dashboard.get_task_list()
    task_names = [task.text for task in task_list]
    assert task_name not in task_names, f'Task "{task_name}" was found in the task list when it should have been deleted.'

@when('the user creates a new task with title new title')
def step_when_user_creates_new_task(context, task_title):
    context.component_pages.click_button_by_css(context.today_dashboard.ADD_TASK_BUTTON_DASHBOARD_SELECTOR)
    time.sleep(1)
    context.component_pages.search_and_fill_by_css_selector(context.new_task.NAME_TASK_FIELD_SELECTOR, task_title)
    time.sleep(1)
    context.component_pages.click_button_by_css(context.new_task.ADD_TASK_BUTTON_FORM_SELECTOR)
    time.sleep(3)

@when('the user marks the task new title as completed')
def step_when_user_marks_task_completed(context, task_title):
    context.today_dashboard.mark_task_completed(task_title)
    time.sleep(3)

@when('the user filters to see completed tasks')
def step_when_user_filters_completed_tasks(context):
    context.component_pages.click_button_by_css(context.view_panel.PRIORITY_DROPDOWN_FILTER_SELECTOR)
    context.component_pages.click_button_by_css(context.view_panel.SELECTED_PRIORITY_ITEM_FILTER_SELECTOR)
    time.sleep(3)

@then('the user should see the task "{task_title}" in the completed tasks list')
def step_then_check_task_in_completed(context, task_title):
    task_list = context.component_pages.get_elements_by_css(context.today_dashboard.TODAY_TASK_CONTENT_SELECTOR)
    assert_is_text_contained_elements(task_list, task_title)