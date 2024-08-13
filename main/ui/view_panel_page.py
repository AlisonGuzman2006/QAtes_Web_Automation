from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class ViewPanelPage:
    PRIORITY_DROPDOWN_FILTER_SELECTOR = 'span[aria-labelledby="view_menu__priority"]'
    SELECTED_PRIORITY_ITEM_FILTER_SELECTOR = 'li[data-value="p1"]'
    VIEW_POPPER_OVERLAY_SELECTOR = 'body > div:nth-child(31)'
    RESET_FILTER_VIEW_PANEL_SELECTOR = 'div[data-testid="popper__overlay"] div[class=" popper"] li[class="menu_item icon_menu_item danger_menu"]'

    DUE_DATE_FILTER_SELECTOR = 'div[data-testid="popper__overlay"] li[aria-labelledby="view_menu__due_date"]'
    DUE_DATE_FILTER_ITEM_SELECTOR = 'div[data-testid="popper__overlay"] li[data-value="NEXT_7_DAYS"]'

    def __init__(self, driver):
        self.driver = driver
        self.EXP_TIMEOUT = 15

    def reset_view_panel(self):
        reset_btn = WebDriverWait(self.driver, self.EXP_TIMEOUT)
        reset_btn.until(lambda: EC.element_to_be_clickable(By.CSS_SELECTOR, self.RESET_FILTER_VIEW_PANEL_SELECTOR))
        reset_btn.click()
        WebDriverWait(self.driver, self.EXP_TIMEOUT).until(lambda: EC.frame_to_be_available_and_switch_to_it()).send_keys(Keys.ESCAPE)
