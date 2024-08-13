import time
from behave import given, when, then
from main.ui.new_task_page import NewTaskPage
from main.ui.todoist_today_page import TodoistTodayPage
from main.ui.component_pages import ComponentPages
from main.ui.view_panel_page import ViewPanelPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from core.assertions.content_assertions import assert_is_text_contained_elements, assert_element_is_deleted


@given('the user is in test in Qates project')
def step_given_user_in_today_dashboard_task_management(context):
    context.component_pages = ComponentPages(context.driver)
    context.today_dashboard = TodoistTodayPage(context.component_pages)
    context.new_task = NewTaskPage(context.driver)
    context.view_panel = ViewPanelPage(context.component_pages)
    context.today_dashboard = TodoistTodayPage(context.component_pages)
    context.component_pages.click_button_by_xpath(context.today_dashboard.TEST_BUTTON_SELECTOR)
    time.sleep(3)

@when('I click on Assignee button')
def click_on_Asignee_button(context):
    time.sleep(2)
    context.component_pages.click_button_by_css(context.today_dashboard.ASSIGNEE_BUTTON_SELECTOR)


@when('I assign the task to a team member')
def assign_the_task_to_a_team_member(context):
    context.component_pages.click_button_by_xpath(context.today_dashboard.ASSIGN_BUTTON_SELECTOR)
    time.sleep(1)
    context.component_pages.action_chains.send_keys(Keys.ESCAPE, Keys.ESCAPE).perform()


@when('the user filters the task to be filter by selected assignee')
def step_filter_task_by_selected_assignee(context):
    context.component_pages.click_button_by_css(context.view_panel.ASSIGNEE_DROPDOWN_FILTER_SELECTOR)
    context.component_pages.click_button_by_css(context.view_panel.SELECTED_ASSIGNEE_ITEM_FILTER_SELECTOR)
    #context.component_pages.action_chains.send_keys(Keys.ESCAPE, Keys.ESCAPE).perform()
    time.sleep(1)



@when('the user filters the task to be filter by a team member')
def step_filter_task_by_team_member(context):
    #context.component_pages.click_button_by_css(context.view_panel.ASSIGNEE_DROPDOWN_FILTER_SELECTOR)
    context.component_pages.click_button_by_xpath(context.view_panel.TEAM_MEMBER_ITEM_FILTER_SELECTOR)
    context.component_pages.click_button_by_xpath(context.view_panel.TEAM_MEMBER_SELECTED_ITEM_FILTER_SELECTOR)
    context.component_pages.action_chains.send_keys(Keys.ESCAPE, Keys.ESCAPE).perform()
    context.component_pages.action_chains.send_keys(Keys.ESCAPE, Keys.ESCAPE).perform()
    time.sleep(1)

@then("the user moves the task created")
def step_impl(context):
    context.component_pages.click_button_by_xpath(context.today_dashboard.MOVE_BUTTON_SELECTOR)
    time.sleep(3)
    context.component_pages.click_button_by_xpath(context.today_dashboard.CONFIRM_MOVE_BUTTON_SELECTOR)
    location_of_task = context.component_pages.web_driver.until(
        EC.presence_of_all_elements_located((By.XPATH, context.today_dashboard.MOVE_BUTTON_SELECTOR))
    )
    assert_is_text_contained_elements(location_of_task, "My Work")

@then('the user should see the task created with the team member assigned in the filtered results')
def step_check_task_is_filtered(context):
    task_list = context.component_pages.web_driver.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, context.today_dashboard.TODAY_TASK_CONTENT_SELECTOR))
    )
    assert_is_text_contained_elements(task_list, "CATherine MICHIel MIAUricio")
    context.today_dashboard.delete_task("CATherine MICHIel MIAUricio")
    context.component_pages.click_button_by_css(context.today_dashboard.VIEW_PANEL_BUTTON_SELECTOR)
    context.view_panel.reset_view_panel()
    time.sleep(1)
