import time

from selenium.webdriver.common.by import By


class TodoistTodayPage:
    TODAY_DASHBOARD_URL = "https://app.todoist.com/app/today"
    ADD_TASK_BUTTON_DASHBOARD_SELECTOR = 'nav > div:nth-of-type(2) > button[type="button"][aria-disabled="false"]'
    VIEW_PANEL_BUTTON_SELECTOR = 'button[aria-label="View options menu"]'

    TODAY_TASKS_CONTAINER_SELECTOR = 'div[context="[object Object]"]'
    TODAY_TASKS_LIST_SELECTOR = 'div[data-item-index]'
    TODAY_TASK_CONTENT_SELECTOR = 'div[class="task_content"]'
    TASK_MORE_ACTIONS_BUTTON_SELECTOR = 'button[data-testid="more_menu"]'
    DIALOG_DELETE_BTN_SELECTOR = 'div[data-testid="modal-overlay"] div[role="dialog"] button[data-autofocus="true"]'

    MENU_ITEM_INBOX_DASHBOARD_SELECTOR = '#todoist_app ul[aria-label="Main filters"]>div[role="button"]'

    TODAY_SECTION_TASK_LIST_SELECTOR = "task_content"
    TODAY_BOTTON_EDIT_SELECTOR = 'button:nth-child(1)'
    TODAY_EDIT_TEXT_SELECTOR = 'p'
    TODAY_SAVE_BTN_SELECTOR = 'button[data-testid="task-editor-submit-button"]'
    TODAY_MARK_COMPLETE_SELECTOR = 'button[aria-label="Mark task as complete"]'

    OPEN_TASK_CREATED_SELECTOR = 'div[role="alert"][aria-live="polite"] > div:nth-of-type(2) > button[type="button"][aria-disabled="false"]'
    EDIT_TASK_NAME_SELECTOR = 'div[data-action-hint="task-detail-view-edit"][aria-label="Task name"]'
    EDIT_TASK_NAME_CONTAINER_SELECTOR = 'div[contenteditable="true"][aria-label="Task name"]'
    SAVE_BUTTON_SELECTOR = 'button[data-testid="task-editor-submit-button"]'
    TASK_TITLE_SELECTOR = '.task_content.task-overview-content-large'
    COMPLETE_CHECKBOX_SELECTOR = 'button[role="checkbox"][data-action-hint="task-detail-view-complete"]'
    TOAST_TITLE_COMPLETED_SELECTOR = '[data-testid="toasts-container"] > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1)'
    MORE_ACTIONS_TASK_SELECTOR = 'button[aria-label="More actions"][aria-haspopup="menu"]'
    DELETE_BUTTON_SELECTOR = 'div[role="menuitem"][data-destructive="true"]'
    CONFIRM_DELETE_BUTTON_SELECTOR = 'button[data-autofocus="true"]'
    TASK_CONTENT_SELECTOR = 'task_content'

    def __init__(self, driver):
        self.driver = driver

    def delete_task(self, task_name):
        task_list = self.driver.find_element(By.CSS_SELECTOR, self.TODAY_TASKS_CONTAINER_SELECTOR)
        task_list_items = task_list.find_elements(By.CSS_SELECTOR, self.TODAY_TASKS_LIST_SELECTOR)
        print(task_list_items, "Iam Here")
        for task_item in task_list_items:
            print(task_item, "Aqui estoy")
            task_content = task_item.find_element(By.CSS_SELECTOR, self.TODAY_TASK_CONTENT_SELECTOR)
            if task_content.text == task_name:
                more_actions_btn = task_item.find_element(By.CSS_SELECTOR, self.TASK_MORE_ACTIONS_BUTTON_SELECTOR)
                more_actions_btn.click()
                time.sleep(5)

                delete_option = self.driver.find_element(By.CSS_SELECTOR, self.MORE_ACTIONS_DELETE_OPTION_SELECTOR)
                delete_option.click()
                time.sleep(5)

                delete_btn_dialog = self.driver.find_element(By.CSS_SELECTOR, self.DIALOG_DELETE_BTN_SELECTOR)
                delete_btn_dialog.click()

                break
        time.sleep(3)

    def navigate_to_inbox_dashboard(self):
        self.driver.find_element(By.CSS_SELECTOR, self.MENU_ITEM_INBOX_DASHBOARD_SELECTOR).click()
        time.sleep(3)
