import time

from selenium.webdriver.common.by import By
class TodoistTodayPage:

    TODAY_DASHBOARD_URL = "https://app.todoist.com/app/today"
    ADD_TASK_BUTTON_DASHBOARD_SELECTOR = '#todoist_app > div.dvqSPB3 > div.app-sidebar-container.Eamj386.fb8d74bb > div._zbmK5I > nav > div.fb8d74bb._14423c92._297575f4.c4a9b3ab._5f8879d9 > button'
    VIEW_PANEL_BUTTON_SELECTOR = 'button[aria-label="View options menu"]'


    TODAY_TASKS_CONTAINER_SELECTOR = 'div[context="[object Object]"]'
    TODAY_TASKS_LIST_SELECTOR = 'div[data-item-index]'
    TODAY_TASK_CONTENT_SELECTOR = 'div[class="task_content"]'
    TASK_MORE_ACTIONS_BUTTON_SELECTOR = 'button[data-testid="more_menu"]'
    MORE_ACTIONS_DELETE_OPTION_SELECTOR = 'div[data-action-hint="task-overflow-menu-delete"]'
    DIALOG_DELETE_BTN_SELECTOR = 'div[data-testid="modal-overlay"] div[role="dialog"] button[data-autofocus="true"]'


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








