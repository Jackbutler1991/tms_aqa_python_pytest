import allure
from page_objects.pages.base_page import BasePage
from page_objects.locators.ebook_page_locators import EbookPageLocators


class EbookPage(BasePage, EbookPageLocators):
    def __init__(self, browser):
        super().__init__(browser)
        self.locator = EbookPageLocators()

    @allure.step("click to open nasa book")
    def click_to_open_nasa_book_page(self):
        self.click_xpath(self.locator.NASA_TO_NOW_BOOK)

    @allure.step("click to open pdf book")
    def click_to_open_nasa_book_pdf(self):
        self.click_xpath(self.locator.NASA_TO_NOW_BOOK_PDF)

    @allure.step("click to open the wind book")
    def click_to_open_the_wind_book_page(self):
        self.click_xpath(self.locator.THE_WIND_BOOK_PAGE)

    @allure.step("click to open pdf book")
    def click_to_open_the_wind_book_pdf(self):
        self.click_xpath(self.locator.THE_WIND_BOOK_PAGE)

    @allure.step("assert open book")
    def assert_if_pdf_the_wind_book_open(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/' \
                              'sites/default/files/atoms/files' \
                              '/the_wind_and_beyond_tagged.pdf'

    @allure.step("assert open book")
    def assert_if_pdf_nasa_book_open(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/sites' \
                              '/default/files/atoms/files/' \
                              'naca_to_nasa_to_now_tagged.pdf'

    @allure.step("click more stories")
    def click_more_stories(self):
        self.click_xpath(self.locator.MORE_STORIES)

    @allure.step("scroll to last book")
    def scroll_to_last_book(self):
        self.scroll_to_element(self.locator.PROBING_THE_SKY)

    @allure.step("assert open more book")
    def assert_open_more_book(self):
        check = self.element_is_visible(self.locator.PROBING_THE_SKY)
        assert check.is_displayed()

    @allure.step("scroll to footer")
    def scroll_to_footer(self):
        self.scroll_to_element(self.locator.ACCESSIBILITY_FOOTER)

    @allure.step("click accessibility on footer")
    def click_accessibility_footer(self):
        self.click_xpath(self.locator.ACCESSIBILITY_FOOTER)

    @allure.step("assert accessibility on footer")
    def assert_accessibility_is_displayed(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/feature' \
                              '/accessibility-statement/'

    @allure.step("scroll to ebook")
    def scroll_to_ebook_footer(self):
        self.scroll_to_element(self.locator.ACCESSIBILITY_FOOTER)

    @allure.step("click on logo")
    def click_logo_footer(self):
        self.click_xpath(self.locator.LOGO_FOOTER)

    @allure.step("check URL")
    def check_url(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/'

    @allure.step("check logo is displayed")
    def check_logo_is_displayed(self):
        check = self.element_is_visible(self.locator.LOGO_FOOTER)
        assert check.is_displayed()
