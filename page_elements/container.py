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