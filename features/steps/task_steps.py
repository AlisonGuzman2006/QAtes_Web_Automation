import time
from behave import given, when, then
from selenium.webdriver import Keys

from main.ui.inbox_dashboard_page import InboxDashboardPage
from main.ui.new_task_page import NewTaskPage
from main.ui.todoist_today_page import TodoistTodayPage
from main.ui.component_pages import ComponentPages
from main.ui.view_panel_page import ViewPanelPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from core.assertions.content_assertions import assert_is_text_contained_elements, assert_element_is_deleted


@given('the user is in the Today page dashboard')
def step_login_to_todoist(context):
    context.component_pages = ComponentPages(context.driver)
    context.today_dashboard = TodoistTodayPage(context.component_pages)
    context.new_task = NewTaskPage(context.driver)
    context.view_panel = ViewPanelPage(context.component_pages)
    context.driver.get(context.today_dashboard.TODAY_DASHBOARD_URL)
    time.sleep(1)


@when('the user opens the new task form')
def step_open_the_the_new_task_form(context):
    context.component_pages.click_button_by_css(context.today_dashboard.ADD_TASK_BUTTON_DASHBOARD_SELECTOR)
    time.sleep(1)


@when('the user fills in the task name')
def step_fill_in_task_name(context):
    context.component_pages.search_and_fill_by_css(context.new_task.NAME_TASK_FIELD_SELECTOR, "Add new Task Feature (added)")
    time.sleep(1)


@when('the user assigns any of the pre-defined priorities to the task')
def step_assign_priority(context):
    context.component_pages.click_button_by_css(context.new_task.SET_PRIORITY_BUTTON_TASK_FORM_SELECTOR)
    context.component_pages.click_button_by_css(context.new_task.SELECTED_PRIORITY_ITEM_SELECTOR)
    time.sleep(1)


@when('the user clicks the "add Task" button')
def step_click_on_add_task_button(context):
    context.component_pages.click_button_by_css(context.new_task.ADD_TASK_BUTTON_FORM_SELECTOR)
    time.sleep(1)


@when('the user opens view filter panel')
def step_open_view_panel(context):
    context.component_pages.click_button_by_css(context.today_dashboard.VIEW_PANEL_BUTTON_SELECTOR)
    time.sleep(1)


@when('the user filters the task to by seen by the priority selected')
def step_filter_task_by_priority(context):
    context.component_pages.click_button_by_css(context.view_panel.PRIORITY_DROPDOWN_FILTER_SELECTOR)
    context.component_pages.click_button_by_css(context.view_panel.SELECTED_PRIORITY_ITEM_FILTER_SELECTOR)
    context.component_pages.action_chains.send_keys(Keys.ESCAPE, Keys.ESCAPE).perform()
    time.sleep(1)


@then('the user should see the task created with the priority assigned in the filtered results')
def step_check_task_is_filtered(context):
    task_list = context.component_pages.web_driver.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, context.today_dashboard.TODAY_TASK_CONTENT_SELECTOR))
    )
    assert_is_text_contained_elements(task_list, "Add new Task Feature (added)")
    context.today_dashboard.delete_task("Add new Task Feature (added)")
    context.component_pages.click_button_by_css(context.today_dashboard.VIEW_PANEL_BUTTON_SELECTOR)
    context.view_panel.reset_view_panel()
    time.sleep(1)


@when('the user sets a due date to the task')
def step_assign_due_date(context):
    context.component_pages.click_button_by_css(context.new_task.DUE_DATE_DROPDOWN_SELECTOR)
    context.component_pages.click_button_by_css(context.new_task.DATE_SELECTOR_TOMORROW_OPTION)
    time.sleep(1)


@when('the user goes to the Inbox dashboard')
def step_go_to_inbox_dashboard(context):
    context.component_pages.click_button_by_css(context.today_dashboard.MENU_ITEM_INBOX_DASHBOARD_SELECTOR)
    time.sleep(1)


@when('the user opens view filter panel from Inbox dashboard')
def step_open_view_panel_from_inbox_dashboard(context):
    context.inbox_dashboard = InboxDashboardPage(context.component_pages)
    context.component_pages.click_button_by_css(context.inbox_dashboard.VIEW_PANEL_BUTTON_SELECTOR)
    time.sleep(1)


@when('the user filters the task to be seen by due date')
def step_filter_task_by_due_date(context):
    context.component_pages.click_button_by_css(context.view_panel.DUE_DATE_FILTER_SELECTOR)
    context.component_pages.click_button_by_css(context.view_panel.DUE_DATE_FILTER_ITEM_SELECTOR)

    context.component_pages.click_button_by_css(context.view_panel.SORTING_DROPDOWN_FILTER_SELECTOR)
    context.component_pages.click_button_by_css(context.view_panel.DUE_DATE_FILTER_SORTING_ITEM_SELECTOR)

    context.component_pages.click_button_by_css(context.view_panel.ORDER_DROPDOWN_FILTER_SELECTOR)
    context.component_pages.click_button_by_css(context.view_panel.ORDER_FILTER_DESCENDING_ITEM_SELECTOR)

    context.component_pages.action_chains.send_keys(Keys.ESCAPE, Keys.ESCAPE).perform()
    time.sleep(1)


@then('the user should see the task created with the due date assigned in the filtered results')
def step_check_task_is_filtered_by_due_date(context):
    task_list = context.component_pages.web_driver.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, context.inbox_dashboard.INBOX_TASK_LIST_CONTENT_SELECTOR))
    )
    assert_is_text_contained_elements(task_list, "Add new Task Feature (added)")
    context.inbox_dashboard.delete_task("Add new Task Feature (added)")
    context.component_pages.click_button_by_css(context.inbox_dashboard.VIEW_PANEL_BUTTON_SELECTOR)
    context.view_panel.reset_view_panel()
    time.sleep(1)

