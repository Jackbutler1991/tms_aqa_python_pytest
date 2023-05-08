import time

from page_objects import BasePage
from locators.container import ContainerLocators

class ContainerElement(BasePage, ContainerLocators):
    def __init__(self, browser):
        super().__init__(browser)

        self.locator = ContainerLocators()

    def asser_that_logo_visible(self):
        assert self.get_element_xpath(self.locator.LOGO)
    def asser_that_logo_visible_ver2(self):
        assert self.locator.LOGO_ver2
    def click_head_menu_missions(self):
        time.sleep(1)
        self.click_xpath(self.locator.HEAD_MISSIONS)
        time.sleep(1)
    def is_displayed_menu_missions(self):
        check = self.get_locator_by_xpath(self.locator.HEAD_MISSIONS_DROPDOWN_OPEN)
        assert check.is_displayed()


