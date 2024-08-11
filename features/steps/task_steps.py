import time
from behave import given, when, then
from selenium.webdriver import Keys
from main.ui.new_task_page import NewTaskPage
from main.ui.todoist_today_page import TodoistTodayPage
from main.ui.component_pages import ComponentPages
from main.ui.view_panel_page import ViewPanelPage

from core.assertions.content_assertions import assert_is_text_contained_elements, assert_element_is_deleted


@given('the user is in the Today page dashboard')
def step_login_to_todoist(context):
    context.component_pages = ComponentPages(context.driver)
    context.today_dashboard = TodoistTodayPage(context.driver)
    context.new_task = NewTaskPage(context.driver)
    context.view_panel = ViewPanelPage(context.driver)
    context.driver.get(context.today_dashboard.TODAY_DASHBOARD_URL)
    time.sleep(3)


@when('the user opens the new task form')
def step_open_the_the_new_task_form(context):
    context.component_pages.click_button_by_css(context.today_dashboard.ADD_TASK_BUTTON_DASHBOARD_SELECTOR)
    time.sleep(3)


@when('the user fills in the task name')
def step_fill_in_task_name(context):
    context.component_pages.search_and_fill_by_css_selector(context.new_task.NAME_TASK_FIELD_SELECTOR, "Antes de mimir")
    time.sleep(3)


@when('the user assigns any of the pre-defined priorities to the task')
def step_assign_priority(context):
    context.component_pages.click_button_by_css(context.new_task.SET_PRIORITY_BUTTON_TASK_FORM_SELECTOR)
    context.component_pages.click_button_by_css(context.new_task.SELECTED_PRIORITY_ITEM_SELECTOR)
    time.sleep(3)


@when('the user clicks the "add Task" button')
def step_click_on_add_task_button(context):
    context.component_pages.click_button_by_css(context.new_task.ADD_TASK_BUTTON_FORM_SELECTOR)
    time.sleep(3)


@when('the user opens view filter panel')
def step_click_on_add_task_button(context):
    context.component_pages.click_button_by_css(context.today_dashboard.VIEW_PANEL_BUTTON_SELECTOR)
    time.sleep(3)


@when('the user filters the task to by seen by the priority selected')
def step_click_on_add_task_button(context):
    dropdown = context.component_pages.click_button_by_css(context.view_panel.PRIORITY_DROPDOWN_FILTER_SELECTOR)
    context.component_pages.click_button_by_css(context.view_panel.SELECTED_PRIORITY_ITEM_FILTER_SELECTOR)
    context.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
    context.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
    time.sleep(3)


@then('the user should see the task created with the priority assigned in the filtered results')
def step_filter_created_task_by_priority(context):
    task_list = context.component_pages.get_elements_by_css(context.today_dashboard.TODAY_TASK_CONTENT_SELECTOR)
    assert_is_text_contained_elements(task_list, "Antes de mimir")
    context.today_dashboard.delete_task("Antes de mimir")
    context.driver.get(context.today_dashboard.TODAY_DASHBOARD_URL)
    context.component_pages.click_button_by_css(context.today_dashboard.VIEW_PANEL_BUTTON_SELECTOR)
    time.sleep(3)
    context.view_panel.reset_view_panel()


