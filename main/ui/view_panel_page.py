from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class ViewPanelPage:
    PRIORITY_DROPDOWN_FILTER_SELECTOR = 'span[aria-labelledby="view_menu__priority"]'
    SELECTED_PRIORITY_ITEM_FILTER_SELECTOR = 'li[data-value="p1"]'
    VIEW_POPPER_OVERLAY_SELECTOR = 'body > div:nth-child(31)'
    RESET_FILTER_VIEW_PANEL_SELECTOR = 'div[data-testid="popper__overlay"] div[class=" popper"] li[class="menu_item icon_menu_item danger_menu"]'

    def __init__(self, driver):
        self.driver = driver

    def reset_view_panel(self):
        reset_btn = self.driver.find_element(By.CSS_SELECTOR, self.RESET_FILTER_VIEW_PANEL_SELECTOR)
        reset_btn.click()
        time.sleep(3)
        self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        time.sleep(3)