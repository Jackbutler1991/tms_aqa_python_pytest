from base_page import BasePage
from page_objects.locators.nasa_page_locators import ContainerLocators


class NasaPage(BasePage, ContainerLocators):
    def __init__(self, browser):
        super().__init__(browser)
        self.locator = ContainerLocators()

    def assert_that_logo_visible(self):
        assert self.get_element_xpath(self.locator.LOGO)

    def bg_card_canvas_is_visible(self):
        check = self.element_is_visible(self.locator.BG_CARD_CANVAS)
        assert check.is_displayed()

    def event_cards_is_visible(self):
        check = self.element_is_visible(self.locator.NASA_EVENTS_CARD)
        assert check.is_displayed()

    def click_head_menu_missions(self):
        self.click_xpath(self.locator.HEAD_MISSIONS)

    def check_elem(self):
        text_element = self.check_text_by_xpath(self.locator.TEXT_IN_FOOTER1)
        print(text_element)
        assert text_element == "National Aeronautics and Space Administration"

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
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/topics/humans-in-space'

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

    def open_privacy_page(self):
        self.click_xpath(self.locator.PRIVACY)
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/about/highlights/HP_Privacy.html'

    def open_accessability_page(self):
        self.click_xpath(self.locator.ACCESSIBILITY)
        current_url = self.get_current_url()
        assert current_url == 'https://www.nasa.gov/feature/accessibility-statement/'

    def open_special_counsel_page(self):
        self.click_xpath(self.locator.SPECIAL_COUNSEL)
        current_url = self.get_current_url()
        assert current_url == 'https://osc.gov/'
