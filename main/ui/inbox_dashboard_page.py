import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main.ui.component_pages import ComponentPages


class InboxDashboardPage:
    TODAY_DASHBOARD_URL = "https://app.todoist.com/app/inbox"
    VIEW_PANEL_BUTTON_SELECTOR = 'button[aria-label="View options menu"]'

    INBOX_TASK_LIST_CONTENT_SELECTOR = 'div[data-testid="virtuoso-item-list"] div[class="task_content"]'
    INBOX_TASK_LIST_CONTAINER = 'div[context="[object Object]"]'
    INBOX_TASK_LIST_SELECTOR = 'div[data-item-index]'
    INBOX_TASK_CONTENT_SELECTOR = 'div[class="task_content"]'
    MORE_ACTIONS_BTN_SELECTOR = 'button[data-testid="more_menu"]'
    MORE_ACTIONS_DELETE_OPTION_SELECTOR = 'div[data-action-hint="task-overflow-menu-delete"]'
    DIALOG_DELETE_BTN_SELECTOR = 'div[data-testid="modal-overlay"] div[role="dialog"] button[data-autofocus="true"]'

    EXP_TIMEOUT = 15

    def __init__(self, driver: ComponentPages):
        self.driver = driver

    def delete_task(self, task_name):
        task_list = self.driver.web_driver.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.INBOX_TASK_LIST_CONTAINER)))
        task_list_items = task_list.find_elements(By.CSS_SELECTOR, self.INBOX_TASK_LIST_SELECTOR)
        for task_item in task_list_items:
            task_content = task_item.find_element(By.CSS_SELECTOR, self.INBOX_TASK_CONTENT_SELECTOR)
            if task_content.text == task_name:
                self.driver.action_chains.move_to_element(task_item).perform()
                more_actions_btn = task_item.find_element(By.CSS_SELECTOR, self.MORE_ACTIONS_BTN_SELECTOR)
                more_actions_btn.click()
                time.sleep(1)

                self.driver.click_button_by_css(self.MORE_ACTIONS_DELETE_OPTION_SELECTOR)
                time.sleep(1)

                self.driver.click_button_by_css(self.DIALOG_DELETE_BTN_SELECTOR)
                break
