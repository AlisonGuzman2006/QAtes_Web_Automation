class Label:
    NEW_FILTER_BUTTON_SELECTOR = 'button[aria-label="Add new filter"]'
    TRY_IT_BUTTON_SELECTOR = "filter-assist-banner"
    FILTER_ASSIST_BUTTON_SELECTOR = "button[aria-label='All tasks due next week']"
    SEND_BUTTON_SELECTOR = 'a[aria-label="Send"]'
    ADD_FILTER_BUTTON_SELECTOR = 'a[aria-label="Add filter"]'
    FILTER_CREATED_POPUP_SELECTOR = "toasts-container"
    OPTIONS_MENU_SELECTOR = 'a[aria-label="Filter options menu"]'
    ADD_FAVORITES_SELECTOR = "div[id=':r3d:']"

    def __init__(self, driver):
        self.driver = driver

