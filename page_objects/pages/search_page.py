import time
import allure
from selenium.webdriver.common.by import By
from page_objects.pages.base_page import BasePage
from page_objects.locators.search_locators import SearchLocators
from page_objects.locators.search_data import SearchData


class Search(BasePage, SearchLocators):
    def __init__(self, browser):
        super().__init__(browser)
        self.locator = SearchLocators()
        self.data = SearchData

    @allure.step("check search is visible")
    def search_is_visible(self):
        check = self.element_is_visible(self.locator.SEARCH)
        assert check.is_displayed()

    @allure.step("find search input")
    def search_input(self):
        self.browser.find_element(By.XPATH,
                                  self.locator.SEARCH_INPUT).send_keys('moon')

    @allure.step("click search")
    def search_click(self):
        self.click_xpath(self.locator.SEARCH_BUTTON)
        time.sleep(1)

    @allure.step("check searched text")
    def check_search_moon(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_MOON)
        print(text_element)
        assert text_element == "News about moon"

    @allure.step("find search input")
    def search_input_special(self):
        self.browser.find_element(By.XPATH,
                                  self.locator.SEARCH_INPUT).send_keys('++-')
        time.sleep(1)

    @allure.step("check searched resalt")
    def check_search_special(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_NO_RESULT)
        print(text_element)
        assert text_element == "Sorry, no results found for" \
                               " '++-'. Try entering fewer or " \
                               "more general search terms."

    @allure.step("input one sumbol in search")
    def search_input_one_symbol(self):
        self.browser.find_element(By.XPATH,
                                  self.locator.SEARCH_INPUT).send_keys('1')

    @allure.step("check text searched one sumbol")
    def check_search_one_symbol(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_NO_RESULT)
        print(text_element)
        assert text_element == "Please enter a search term in the box above."

    @allure.step("input 255 sumbol in search")
    def search_input_more255_symbol(self):
        self.browser.find_element(By.XPATH, self.locator.SEARCH_INPUT)
        self.browser.send_keys(self.data.SEARCH_MORE255_SYMBOLS)

    @allure.step("check text searched 255 sumbol")
    def check_search_more255_symbol(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_NO_RESULT)
        print(text_element)
        assert text_element == "Your search term is too long." \
                               " Try again using a shorter word or phrase."

    @allure.step("input another language in search")
    def search_input_another_language(self):
        self.browser.find_element(By.XPATH, self.locator.
                                  SEARCH_INPUT).send_keys('луна')

    @allure.step("check text searched another language")
    def check_search_another_language(self):
        text_element = self.check_text_by_xpath(self.locator.SEARCH_NO_RESULT)
        print(text_element)
        assert text_element == "Sorry, no results found for " \
                               "'луна'. Try entering fewer or " \
                               "more general search terms."

    @allure.step("push Enter from keyboard")
    def enter(self):
        self.push_enter(self.locator.SEARCH_INPUT)
