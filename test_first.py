import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By


def test_deleviry(browser):
##    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
##    driver.implicitly_wait(10)
    browser.get('https://teachmeskills.by/kursy-programmirovaniya/qa-avtomatizirovannoe-testirovanie-na-python-online')

#    driver.add_cookie({'name':'TEST_sbjs_first', 'value':'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7'
#                                                    'C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29'})

    selector = browser.find_element(By.CLASS_NAME, 't517__sectioninfowrapper')
    selectors = browser.find_elements(By.CLASS_NAME, 't517__sectioninfowrapper')
    print(selectors)

#    cookie_loc = (By.ID, "modal-cookie")
#    cookie_sel = driver.find_element(*cookie_loc)
#    driver.execute_script("arguments[0].setAttribute('display', 'none')", cookie_sel)

    browser.maximize_window()

#    footer_xpath = (By.XPATH, '//*[@id="footer-inner"]/div/div/div[1]/div[1]/div[2]/a')
#    footer_locator = driver.find_element(*footer_xpath)

#    driver.execute_script("arguments[0].scrollIntoView();", footer_locator)

#    footer_locator.click()
#    driver.fullscreen_window()
    current_url = browser.current_url
    assert current_url == 'https://teachmeskills.by/kursy-programmirovaniya/qa-avtomatizirovannoe-testirovanie-na-python-online'
#    assert cookie_sel.is_displayed()

##    driver.close()


def test_deleviry_21_vek(browser):
    browser.get('https://www.youtube.com/')

#    driver.add_cookie({'name':'TEST_sbjs_first', 'value':'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7'
#                                                    'C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29'})
    selector = browser.find_element(By.XPATH, '//*[@id="contents"]')
    print(selector)

    browser.maximize_window()

    current_url = browser.current_url
    assert current_url == 'https://www.youtube.com/'
#    assert cookie_sel.is_displayed()
