from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main.ui.component_pages import ComponentPages

class ViewPanelPage:
    PRIORITY_DROPDOWN_FILTER_SELECTOR = 'span[aria-labelledby="view_menu__priority"]'
    SORTING_DROPDOWN_FILTER_SELECTOR = 'li[aria-labelledby="view_menu__sort_by"]'
    ORDER_DROPDOWN_FILTER_SELECTOR = 'li[aria-labelledby="view_menu__order"]'
    
    SELECTED_PRIORITY_ITEM_FILTER_SELECTOR = 'li[data-value="p1"]'
    VIEW_POPPER_OVERLAY_SELECTOR = 'body > div:nth-child(31)'
    RESET_FILTER_VIEW_PANEL_SELECTOR = 'div[data-testid="popper__overlay"] div[class=" popper"] li[class="menu_item icon_menu_item danger_menu"]'

    ORDER_FILTER_DESCENDING_ITEM_SELECTOR = 'div[data-testid="popper__overlay"] li[data-value="DESC"]'
    DUE_DATE_FILTER_SORTING_ITEM_SELECTOR = 'div[data-testid="popper__overlay"] li[data-value="DUE_DATE"]'
    DUE_DATE_FILTER_SELECTOR = 'div[data-testid="popper__overlay"] li[aria-labelledby="view_menu__due_date"]'
    DUE_DATE_FILTER_ITEM_SELECTOR = 'div[data-testid="popper__overlay"] li[data-value="NEXT_7_DAYS"]'

    ASSIGNEE_DROPDOWN_FILTER_SELECTOR = 'span[aria-labelledby="view_menu__assigned"]'
    SELECTED_ASSIGNEE_ITEM_FILTER_SELECTOR = 'li[data-value="assigned to:"]'
    TEAM_MEMBER_ITEM_FILTER_SELECTOR = "//span[text()='Choose assignees']"
    TEAM_MEMBER_SELECTED_ITEM_FILTER_SELECTOR = "//div[@class='person_picker__option_text' and text()='Freddy']"


    def __init__(self, driver: ComponentPages):
        self.driver = driver

    def reset_view_panel(self):
        self.driver.click_button_by_css(self.RESET_FILTER_VIEW_PANEL_SELECTOR)
        self.driver.action_chains.send_keys(Keys.ESCAPE).perform()
