import time

from selenium.webdriver.common.by import By

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

    def search_is_visible(self):
        check = self.element_is_visible(self.locator.SEARCH)
        assert check.is_displayed()
    def bg_card_canvas_is_visible(self):
        check = self.element_is_visible(self.locator.BG_CARD_CANVAS)
        assert check.is_displayed()

    def event_cards_is_visible(self):
        check = self.element_is_visible(self.locator.NASA_EVENTS_CARD)
        assert check.is_displayed()

    def click_head_menu_missions(self):
        time.sleep(1)
        self.click_xpath(self.locator.HEAD_MISSIONS)
        time.sleep(1)

    def check_elem(self):
        text_element = self.check_text_by_xpath(self.locator.TEXT_IN_FOOTER1)
        print(text_element)
        assert text_element == "National Aeronautics and Space Administration"

    def check_in_sucsessfull(self):
        text_element = self.check_text_by_xpath(self.locator.SING_IN_SUCCESSFUL)
        print(text_element)
        assert text_element == "Sign in Successful."

    def text_nasa_events(self):
        text_element = self.check_text_by_xpath(self.locator.TEXT_NASA_EVENTS)
        print(text_element)
        assert text_element == "NASA Events"

    def text_nasa_tv_shedule(self):
        text_element = self.check_text_by_xpath(self.locator.TEXT_NASA_TV_SCHEDULE)
        print(text_element)
        assert text_element == "NASA TV Schedule"

    def text_nasa_launches(self):
        text_element = self.check_text_by_xpath(self.locator.TEXT_NASA_LAUNCHES)
        print(text_element)
        assert text_element == "Launches and Landings"

    def is_displayed_menu_missions(self):
        check = self.get_locator_by_xpath(self.locator.HEAD_MISSIONS_DROPDOWN_OPEN)
        assert check.is_displayed()
    def click_head_menu_galleries(self):
        self.get_locator_by_xpath(self.locator.HEAD_GALLERIES)
    def is_displayed_menu_galleries(self):
        check = self.get_locator_by_xpath(self.locator.HEAD_GALLERIES_DROPDOWN_OPEN)
        assert check.is_displayed()
    def click_head_menu_humans_in_space(self):
        self.click_xpath(self.locator.HUMANS_IN_SPACE)
    def check_open_page_humans_in_space(self):
        time.sleep(1)
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/topics/humans-in-space'
    def singin_fqia(self):
        self.browser.get('https://pal.hq.nasa.gov/app/PalLogin.aspx')
        self.browser.find_element(By.XPATH, '//*[@id="uxUserName"]').send_keys(self.TEST_LOGIN)
        self.browser.find_element(By.XPATH, '//*[@id="uxPassword"]').send_keys(self.TEST_PASSWORD)

    def singin_fqia_neg1(self):
        self.browser.get('https://pal.hq.nasa.gov/app/PalLogin.aspx')
        self.browser.find_element(By.XPATH, '//*[@id="uxUserName"]').send_keys(self.TEST_LOGIN_1)
        self.browser.find_element(By.XPATH, '//*[@id="uxPassword"]').send_keys(self.TEST_PASSWORD_1)

    def singin_fqia_neg2(self):
        self.browser.get('https://pal.hq.nasa.gov/app/PalLogin.aspx')

    def click_head_menu_humans_in(self):
        self.click_xpath(self.locator.SIGN_IN_BUTTON)

    def test_test(self):
#        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, locator))
        ck = self.browser.switch_to.frame(self.browser.find_element(By.XPATH, '//*[@id="validationmessage"]'))
        print(ck)


#        sk = self.browser.switch_to.frame(self.browser.find_element(By.XPATH, '//*[@id="errorModal"]/div/div/div[1]/h4'))
#        print(sk)
#        check_text = self.browser.find_element(By.XPATH, '//*[@id="errorModal"]/div/div/div[1]/h4')
#        check_text_1 = check_text.getText()


#

#        text = self.browser.find_element(By.XPATH, '//*[@id="errorModal"]//h4')
#        text_test = text.getText();

#        print(text_test)
#        assert text = '//*[@id="errorModal"]//h4'

    def open_flight_page(self):
        self.click_xpath(self.locator.FLIGHT)
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/topics/aeronautics/index.html'

    def open_solar_system_page(self):
        self.click_xpath(self.locator.SOLAR_SUSTEM)
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/topics/solarsystem/index.html'

    def open_stem_engagement_page(self):
        self.click_xpath(self.locator.STEM_ENGAGEMENT)
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/stem'

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