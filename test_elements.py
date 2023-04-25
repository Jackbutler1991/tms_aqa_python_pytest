from selenium.webdriver.common.by import By

from Helpers import BasePage
from ElementsObject import ElementsObject

def test_21(browser):
    base_page = BasePage(browser)
    base_page.browser.get('https://ultimateqa.com/simple-html-elements-for-automation/')
    base_page.click(ElementsObject.radio_button)
    browser.save_screenshot("test1(2).png")
    assert base_page.assert_that_element_is_selected(ElementsObject.radio_button)

 # div[@class="et_pb_button_wrapper"]
def test_BBC1_xpath(browser):
    base_page = BasePage(browser)
    base_page.browser.get('https://www.bbc.com/news')
    base_page.get_locator_by_contains('gs-c-promo-image')

def test_BBC2_xpath(browser):
    base_page = BasePage(browser)
    base_page.browser.get('https://www.bbc.com/news')
    base_page.get_locator_by_contains('orb-nav-section orb-nav-blocks')

def test_BBC3_css(browser):
    base_page = BasePage(browser)
    base_page.browser.get('https://www.bbc.com/news')
    base_page.get_locator_by_css('.orb-nav-section.orb-nav-blocks')

def test_BBC4_css(browser):
    base_page = BasePage(browser)
    base_page.browser.get('https://www.bbc.com/news')
    base_page.get_locator_by_css('.orb-nav-sport')