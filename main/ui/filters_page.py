class Filters:
    NEW_FILTER_BUTTON_SELECTOR = 'button[aria-label="Add new filter"]'
    TRY_IT_BUTTON_SELECTOR = 'button[data-gtm-id="filter-assist-banner"]'
    FILTER_ASSIST_BUTTON_SELECTOR = "button[aria-label='All tasks due next week']"
    SEND_BUTTON_SELECTOR = 'button[aria-label="Send"]'
    ADD_FILTER_BUTTON_SELECTOR = 'button[aria-label="Add filter"]'
    FILTER_CREATED_POPUP_SELECTOR = 'div[data-testid="toasts-container"]'
    OPTIONS_MENU_SELECTOR = 'button[aria-label="Filter options menu"]'
    ADD_FAVORITES_SELECTOR = 'div[data-track="filters|menu_add_to_favorites"]'
    REMOVE_FAVORITES_SELECTOR = 'div[data-dialog][role="menu"] > div:nth-of-type(2) > div:first-of-type'
    FILTER_OPTION_SELECTOR = 'ul[aria-label="Filters"] > div:nth-of-type(1) > li:nth-of-type(1)'
    FILTER_TEXT_SELECTOR = 'simple_content'
    DELETE_FILTER_BUTTON_SELECTOR = 'div[data-track="filters|menu_delete"]'
    CONFIRM_DELETE_BUTTON_SELECTOR = 'button[data-autofocus="true"][type="button"][aria-disabled="false"]'
    MORE_OPTIONS_FILTER_SELECTOR = 'button[aria-label="Filter options menu"]'
    EMPTY_FILTERS_SELECTOR = 'section[aria-label="Filters"][data-testid="section"] > div:nth-of-type(1)'

    def __init__(self, driver):
        self.driver = driver
