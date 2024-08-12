import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

    MENU_ITEM_INBOX_DASHBOARD_SELECTOR = '#todoist_app ul[aria-label="Main filters"]>div[role="button"]'

    TODAY_SECTION_TASK_LIST_SELECTOR = 'div[class="view_content"]>section:nth-child(2) div[data-index]'
    TODAY_BOTTON_EDIT_SELECTOR = 'button:nth-child(1)'
    TODAY_EDIT_TEXT_SELECTOR = 'p'
    TODAY_SAVE_BTN_SELECTOR = 'button[data-testid="task-editor-submit-button"]'


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

    def edit_task(self):
           #task_list = self.driver.find_element(By.CSS_SELECTOR, self.TODAY_TASKS_CONTAINER_SELECTOR)
            task_list_items = self.driver.find_elements(By.CSS_SELECTOR, self.TODAY_SECTION_TASK_LIST_SELECTOR)

            for task_item in task_list_items:
                task_content = task_item.find_element(By.CSS_SELECTOR, self.TODAY_TASK_CONTENT_SELECTOR)
                if task_content.text == "New Task":
                    selected_task = task_item.find_element(By.CSS_SELECTOR, self.TODAY_BOTTON_EDIT_SELECTOR)
                    selected_task.click()
                    time.sleep(2)

                    title_task = task_item.find_element(By.CSS_SELECTOR, self.TODAY_EDIT_TEXT_SELECTOR)
                    title_task.clear()
                    title_task.send_keys("New Title")

                    btn_save = self.driver.find_element(By.CSS_SELECTOR, self.TODAY_SAVE_BTN_SELECTOR)
                    btn_save.click()

                    break  # Terminamos de buscar una vez que se ha encontrado y editado la tare




    def delete_task_management(self, task_name):
        task_list_items = self.driver.find_elements(By.CSS_SELECTOR, self.TODAY_SECTION_TASK_LIST_SELECTOR)
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



