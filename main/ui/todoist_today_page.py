import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from main.ui.component_pages import ComponentPages

class TodoistTodayPage:
    TODAY_DASHBOARD_URL = "https://app.todoist.com/app/today"
    ADD_TASK_BUTTON_DASHBOARD_SELECTOR = 'nav > div:nth-of-type(2) > button[type="button"][aria-disabled="false"]'
    VIEW_PANEL_BUTTON_SELECTOR = 'button[aria-label="View options menu"]'


    TODAY_TASKS_CONTAINER_SELECTOR = 'div.list_holder div[data-testid="virtuoso-item-list"]'
    TODAY_TASKS_LIST_SELECTOR = 'div[data-item-index]'
    TODAY_TASK_CONTENT_SELECTOR = 'div.task_content'
    TASK_MORE_ACTIONS_BUTTON_SELECTOR = 'button[data-testid="more_menu"]'
    DIALOG_DELETE_BTN_SELECTOR = 'div[data-testid="modal-overlay"] div[role="dialog"] button[data-autofocus="true"]'
    MENU_ITEM_INBOX_DASHBOARD_SELECTOR = '#todoist_app ul[aria-label="Main filters"]>div[role="button"]'

    def __init__(self, driver: ComponentPages):
        # here is the web driver wait from component pages
        self.driver = driver

    def delete_task(self, task_name):
        task_list = self.driver.web_driver.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.TODAY_TASKS_CONTAINER_SELECTOR)))
        task_list_items = task_list.find_elements(By.CSS_SELECTOR, self.TODAY_TASKS_LIST_SELECTOR)
        for task_item in task_list_items:
            task_content = task_item.find_element(By.CSS_SELECTOR, self.TODAY_TASK_CONTENT_SELECTOR)
            print(task_content.text, 'text')
            if task_content.text == task_name:
                self.driver.action_chains.move_to_element(task_item).perform()
                more_actions_btn = task_item.find_element(By.CSS_SELECTOR, self.TASK_MORE_ACTIONS_BUTTON_SELECTOR)
                more_actions_btn.click()
                time.sleep(1)

                self.driver.click_button_by_css(self.MORE_ACTIONS_DELETE_OPTION_SELECTOR)
                time.sleep(1)

                self.driver.click_button_by_css(self.DIALOG_DELETE_BTN_SELECTOR)
                break

    def navigate_to_inbox_dashboard(self):
        self.driver.find_element(By.CSS_SELECTOR, self.MENU_ITEM_INBOX_DASHBOARD_SELECTOR).click()
        time.sleep(3)
