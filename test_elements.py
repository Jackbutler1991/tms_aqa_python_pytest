import time

from selenium.webdriver.common.by import By

from Helpers import BasePage
from ElementsObject import ElementsObject

def test_21(browser):
    base_page = BasePage(browser)
    base_page.browser.get('https://ultimateqa.com/simple-html-elements-for-automation/')
    base_page.click(ElementsObject.radio_button)
    browser.save_screenshot("test1(2).png")
    assert base_page.assert_that_element_is_selected(ElementsObject.radio_button)

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
    base_page.get_locator_by_contains('.orb-nav-sport')

#Practice1
def test_alert(browser):
    base_page = BasePage(browser)
    base_page.browser.get('https://learn.javascript.ru/task/simple-page')
    base_page.click(ElementsObject.run_demo)
    prompt = browser.switch_to.alert
    prompt.send_keys("Alexander")
    prompt.accept()
    time.sleep(2)
    assert prompt.text == "Alexander"
#Practice 3
def test_iframe(browser):
    base_page = BasePage(browser)
    base_page.browser.get('http://the-internet.herokuapp.com/iframe')
    base_page.open_iframe(ElementsObject.iframe)
    check_text = browser.find_element(By.XPATH, ElementsObject.iframe_text)
    assert check_text.text == "Your content goes here."

#hw22
def test_check_uncheck(browser):
    base_page = BasePage(browser)
    base_page.browser.get('http://the-internet.herokuapp.com/')
    base_page.click_xpath('.//*[@id="content"]//li[6]/a')
    base_page.click_xpath(ElementsObject.checkbox1)
    base_page.click_xpath(ElementsObject.checkbox2)
    assert base_page.assert_that_element_is_selected_xpath(ElementsObject.checkbox1)
    assert base_page.assert_that_element_is_not_selected_xpath(ElementsObject.checkbox2)

def test_scroll(browser):
    base_page = BasePage(browser)
    base_page.browser.get('http://the-internet.herokuapp.com/')
    base_page.browser.fullscreen_window()
    check = base_page.scroll_to_xpath(ElementsObject.scroll)
    time.sleep(1)
    assert check.is_displayed()

def test_check_radiobatton(browser):
    base_page = BasePage(browser)
    base_page.browser.get('https://demoqa.com/')
    base_page.click_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]')
    base_page.click_xpath('//*[@id="app"]//div[1]/span/div')
    base_page.click_xpath('//*[@id="item-2"]')
    base_page.click_xpath(ElementsObject.radio_button1)
    time.sleep(1)
    browser.save_screenshot("test(Radio)button).png")
    text = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p/span')
    assert text.text  == 'Impressive'

def test_select_value_from_dropdown(browser):
    base_page = BasePage(browser)
    base_page.browser.get('https://demoqa.com/select-menu')
    base_page.select_value_from_dropdown(ElementsObject.elem1)
    base_page.select_value_from_dropdown(ElementsObject.elem2)
    time.sleep(1)
    select_elem1 = base_page.get_text(ElementsObject.elem_test)
    time.sleep(1)
    assert select_elem1 == "Group 2, option 1"


