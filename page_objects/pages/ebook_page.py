from page_objects.pages.base_page import BasePage
from page_objects.locators.ebook_page_locators import EbookPageLocators


class EbookPage(BasePage, EbookPageLocators):
    def __init__(self, browser):
        super().__init__(browser)
        self.locator = EbookPageLocators()

    def click_to_open_nasa_book_page(self):
        self.click_xpath(self.locator.NASA_TO_NOW_BOOK)

    def click_to_open_nasa_book(self):
        self.click_xpath(self.locator.NASA_TO_NOW_BOOK_PDF)

    def assert_if_pdf_nasa_book_open(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/sites/default' \
                              '/files/atoms/files/naca_to_nasa_to_now_tagged.pdf'