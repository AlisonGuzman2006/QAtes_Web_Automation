class NewTaskPage:

    ADD_TASK_BUTTON_FORM_SELECTOR = 'button[data-testid="task-editor-submit-button"]'
    NAME_TASK_FIELD_SELECTOR = 'div[aria-label="Task name"]'
    SET_PRIORITY_BUTTON_TASK_FORM_SELECTOR = 'div[aria-label="Set priority"][aria-expanded="false"]'
    SELECTED_PRIORITY_ITEM_SELECTOR = 'li[data-action-hint="task-actions-priority-4"]'

    DUE_DATE_DROPDOWN_SELECTOR = 'div[aria-label="Set due date"]'
    SELECTED_DUE_DATE_ITEM_SELECTOR = 'div[data-testid="popper__overlay"] button[data-track="scheduler|date_shortcut_nextweekend"]'
    
    DATE_SELECTOR_TOMORROW_OPTION = 'button[data-action-hint="scheduler-suggestion-tomorrow"]'

    def __init__(self, driver):
        self.driver = driver
