import time
from behave import given, when, then

from main.ui.new_task_page import NewTaskPage
from main.ui.todoist_today_page import TodoistTodayPage
from main.ui.component_pages import ComponentPages
from main.ui.view_panel_page import ViewPanelPage


@given('the user is in the Today page dashboard for task management')
def step_given_user_in_today_dashboard_task_management(context):
    context.component_pages = ComponentPages(context.driver)
    context.today_dashboard = TodoistTodayPage(context.component_pages)
    context.new_task = NewTaskPage(context.driver)
    context.view_panel = ViewPanelPage(context.component_pages)
    context.today_dashboard = TodoistTodayPage(context.component_pages)
    time.sleep(3)


@when('the user creates a new task with title "{task_title}"')
def step_when_user_creates_new_task(context, task_title):
    context.component_pages.click_button_by_css(context.today_dashboard.ADD_TASK_BUTTON_DASHBOARD_SELECTOR)
    context.component_pages.search_and_fill_by_css(context.new_task.NAME_TASK_FIELD_SELECTOR, task_title)
    context.component_pages.click_button_by_css(context.new_task.ADD_TASK_BUTTON_FORM_SELECTOR)
    time.sleep(3)


@when('the user edits the task with new title {new_task_title}')
def step_when_user_edits_task(context, new_task_title):
    context.component_pages.click_button_by_css(context.today_dashboard.EDIT_TASK_NAME_SELECTOR)
    context.component_pages.search_clean_and_fill_by_css(context.new_task.NAME_TASK_FIELD_SELECTOR, new_task_title)
    time.sleep(3)
    context.component_pages.click_button_by_css(context.today_dashboard.SAVE_BUTTON_SELECTOR)


@when('the user open the new task')
def step_when_user_edits_task(context):
    context.component_pages.click_button_by_css(context.today_dashboard.OPEN_TASK_CREATED_SELECTOR)
    time.sleep(2)


@then('the user should see the new title task {new_task_title}')
def step_when_user_edits_task(context, new_task_title):
    text = context.component_pages.get_text_by_css_selector(context.today_dashboard.TASK_TITLE_SELECTOR)
    assert text == new_task_title, "Wrong text"


@when('the user marks the task as completed')
def step_when_user_marks_task_completed(context):
    context.component_pages.click_button_by_css(context.today_dashboard.COMPLETE_CHECKBOX_SELECTOR)
    time.sleep(3)


@then('the user should see a toast with the title "{task_completed}"')
def step_then_check_task_in_completed(context, task_completed):
    text = context.component_pages.get_text_by_css_selector(context.today_dashboard.TOAST_TITLE_COMPLETED_SELECTOR)
    assert text == task_completed, "Wrong text"


@then('the user should not see "{delete_task}"')
def step_impl(context, delete_task):
    tasks = context.component_pages.get_elements_by_class(context.today_dashboard.TASK_CONTENT_SELECTOR)
    target_task = None
    for task in tasks:
        if delete_task in task.text:
            target_task = task
            break
    assert target_task is None, f"Target task is not equal to none, it is {delete_task}"


@when("the user deletes the task created")
def step_impl(context):
    context.component_pages.click_button_by_css(context.today_dashboard.MORE_ACTIONS_TASK_SELECTOR)
    context.component_pages.click_button_by_css(context.today_dashboard.DELETE_BUTTON_SELECTOR)
    time.sleep(3)
    context.component_pages.click_button_by_css(context.today_dashboard.CONFIRM_DELETE_BUTTON_SELECTOR)