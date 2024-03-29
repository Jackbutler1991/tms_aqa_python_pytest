import allure
from page_objects.pages.base_page import BasePage
from page_objects.locators.nasa_page_locators import ContainerLocators


class NasaPage(BasePage, ContainerLocators):
    def __init__(self, browser):
        super().__init__(browser)
        self.locator = ContainerLocators()

    @allure.step("check logo is visible")
    def assert_that_logo_visible(self):
        assert self.get_element_xpath(self.locator.LOGO)

    @allure.step("check bg card")
    def bg_card_canvas_is_visible(self):
        check = self.element_is_visible(self.locator.BG_CARD_CANVAS)
        assert check.is_displayed()

    @allure.step("assert event card is visible")
    def event_cards_is_visible(self):
        check = self.element_is_visible(self.locator.NASA_EVENTS_CARD)
        assert check.is_displayed()

    @allure.step("click head menu")
    def click_head_menu_missions(self):
        self.click_xpath(self.locator.HEAD_MISSIONS)

    @allure.step("check National aeronautics")
    def check_elem(self):
        text_element = self.check_text_by_xpath(self.locator.TEXT_IN_FOOTER1)
        print(text_element)
        assert text_element == "National Aeronautics and Space Administration"

    @allure.step("check Nasa Events text")
    def check_text_nasa_events(self):
        text_element = self.check_text_by_xpath(self.locator.TEXT_NASA_EVENTS)
        print(text_element)
        assert text_element == "NASA Events"

    @allure.step("check Nasa TV Schedule")
    def text_nasa_tv_shedule(self):
        text_element = self.check_text_by_xpath(self.locator.NASA_TV_SCHEDULE)
        print(text_element)
        assert text_element == "NASA TV Schedule"

    @allure.step("check text Launches and Landings")
    def check_text_nasa_launches(self):
        text_elem = self.check_text_by_xpath(self.locator.TEXT_NASA_LAUNCHES)
        print(text_elem)
        assert text_elem == "Launches and Landings"

    @allure.step("assert is displayed missions")
    def assert_is_displayed_menu_missions(self):
        check = self.get_locator_by_xpath(self.locator.HEAD_MIS_DROP_OPEN)
        assert check.is_displayed()

    @allure.step("click head menu galleries")
    def click_head_menu_galleries(self):
        self.get_locator_by_xpath(self.locator.HEAD_GALLERIES)

    @allure.step("check is displayed menu galleries")
    def assert_is_displayed_menu_galleries(self):
        check = self.get_locator_by_xpath(self.locator.HEAD_GAL_DROP_OPEN)
        assert check.is_displayed()

    @allure.step("click head menu missions")
    def click_head_menu_humans_in_space(self):
        self.click_xpath(self.locator.HUMANS_IN_SPACE)

    @allure.step("check open page human in spase")
    def check_open_page_humans_in_space(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/topics/humans-in-space'

    @allure.step("open flight page")
    def open_flight_page(self):
        self.click_xpath(self.locator.FLIGHT)

    @allure.step("check open flight page")
    def chek_open_flight_page(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/topics/' \
                              'aeronautics/index.html'

    @allure.step("open solar sustem page")
    def open_solar_system_page(self):
        self.click_xpath(self.locator.SOLAR_SUSTEM)

    @allure.step("check open solar sustem page")
    def check_open_solar_system_page(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/' \
                              'topics/solarsystem/index.html'

    @allure.step("open stem engagement page")
    def open_stem_engagement_page(self):
        self.click_xpath(self.locator.STEM_ENGAGEMENT)

    @allure.step("check open stem engagement page")
    def check_open_stem_engagement_page(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/stem'

    @allure.step("open privacy page")
    def open_privacy_page(self):
        self.click_xpath(self.locator.PRIVACY)

    @allure.step("check open privacy page")
    def check_open_privacy_page(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/about/' \
                              'highlights/HP_Privacy.html'

    @allure.step("open accessability page")
    def open_accessability_page(self):
        self.click_xpath(self.locator.ACCESSIBILITY)

    @allure.step("check open accessability page")
    def check_open_accessability_page(self):
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/feature' \
                              '/accessibility-statement/'

    @allure.step("open special counsel page")
    def open_special_counsel_page(self):
        self.click_xpath(self.locator.SPECIAL_COUNSEL)

    @allure.step("checkopen special counsel page")
    def check_open_special_counsel_page(self):
        current_url = self.get_current_url()
        assert current_url == 'https://osc.gov/'

    @allure.step("fined follow Nasa")
    def find_categories(self):
        self.get_locator_by_xpath(self.locator.FOLLOW_NASA_CATEGORIES)

    @allure.step("clicked Follow Nasa")
    def click_follow_nasa(self):
        self.mouse_moving(self.locator.FOLLOW_NASA_CATEGORIES)
        self.click(self.locator.FOLLOW_NASA_SPOT_STATION)

    @allure.step("click learn where")
    def click_learn_where(self):
        self.click(self.locator.LEARN_WHERE_TO_LOOK)

    @allure.step("click live ISS")
    def click_live_iss(self):
        self.click(self.locator.LIVE_ISS)

    @allure.step("click Follow Nasa")
    def click_see_all_faqs(self):
        self.click(self.locator.SEE_ALL_FAQS)

    @allure.step("asserted main page is change")
    def asser_change_main_page_url(self):
        assert self.current_url() != "https://spotthestation.nasa.gov/"
