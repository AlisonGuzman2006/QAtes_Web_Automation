class NewTaskPage:

    NAME_TASK_FIELD_SELECTOR = 'p[data-placeholder="Task name"]'
    ADD_TASK_BUTTON_FORM_SELECTOR = 'button[data-testid="task-editor-submit-button"]'
    SET_PRIORITY_BUTTON_TASK_FORM_SELECTOR = 'div[aria-label="Set priority"][aria-expanded="false"]'
    SELECTED_PRIORITY_ITEM_SELECTOR = 'li[data-action-hint="task-actions-priority-4"]'

    def __init__(self, driver):
        self.driver = driver
