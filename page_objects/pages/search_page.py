import time
from selenium.webdriver.common.by import By
from base_page import BasePage
from page_objects.locators.search_locators import SearchLocators


class Search(BasePage, SearchLocators):
    def __init__(self, browser):
        super().__init__(browser)
        self.locator = SearchLocators()
    def search_is_visible(self):
        check = self.element_is_visible(self.locator.SEARCH)
        assert check.is_displayed()

    def search_input(self):
        self.browser.find_element(By.XPATH, self.locator.SEARCH_INPUT).send_keys('moon')
        time.sleep(1)

    def search_click(self):
        self.click_xpath(self.locator.SEARCH_BUTTON)
        time.sleep(1)

    def text_search_moon(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_MOON)
        print(text_element)
        assert text_element == "News about moon"

    def search_input_special(self):
        self.browser.find_element(By.XPATH, self.locator.SEARCH_INPUT).send_keys('++-')
        time.sleep(1)

    def text_search_special(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_NO_RESULT)
        print(text_element)
        assert text_element == "Sorry, no results found for '++-'. Try entering fewer or more general search terms."

    def search_input_one_symbol(self):
        self.browser.find_element(By.XPATH, self.locator.SEARCH_INPUT).send_keys('1')

    def text_search_one_symbol(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_NO_RESULT)
        print(text_element)
        assert text_element == "Please enter a search term in the box above."

    def search_input_more255_symbol(self):
        self.browser.find_element(By.XPATH, self.locator.SEARCH_INPUT).send_keys(self.locator.SEARCH_MORE255_SYMBOLS)

    def text_search_more255_symbol(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_NO_RESULT)
        print(text_element)
        assert text_element == "Your search term is too long. Try again using a shorter word or phrase."

    def search_input_another_language(self):
        self.browser.find_element(By.XPATH, self.locator.SEARCH_INPUT).send_keys('луна')

    def text_search_another_language(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_NO_RESULT)
        print(text_element)
        assert text_element == "Sorry, no results found for 'луна'. Try entering fewer or more general search terms."

    def enter(self):
        self.push_enter(self.locator.SEARCH_INPUT)
