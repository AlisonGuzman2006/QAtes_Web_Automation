class Label:
    FILTERS_AND_LABEL_SELECTOR = 'a[aria-label="Filters & Labels"]'
    NEW_LABEL_BUTTON_SELECTOR = 'button[aria-label="Add new label"]'
    LABEL_NAME_FIELD_SELECTOR = "edit_label_modal_field_name"
    ADD_LABEL_BUTTON_SELECTOR = 'button[type="submit"]'
    ADD_NEW_TASK_BUTTON_SELECTOR = 'button[type="button"][data-supports-active-task="true"]'
    NAME_TASK_FIELD_SELECTOR = 'div[aria-label="Task name"][contenteditable="true"]'
    ADD_TASK_BUTTON_SELECTOR = 'button[type="submit"][data-testid="task-editor-submit-button"]'
    TASK_TITTLE_SELECTOR = "task_content"
    LABELS_SELECTOR = "simple_content"
    LABEL_MENU_SELECTOR = 'button[aria-label="Label options menu"]'
    LABEL_DELETE_BUTTON_SELECTOR = 'div[data-track="labels|menu_delete"]'
    DELETE_BUTTON_SELECTOR = '[data-autofocus="true"][type="button"][aria-disabled="false"]'

    def __init__(self, driver):
        self.driver = driver
