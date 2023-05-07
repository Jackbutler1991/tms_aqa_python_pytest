from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def get_locator_by_css(self, selector):
        # .slass_name
        css = (By.CSS_SELECTOR, selector)
        return self.browser.find_element(*css)

    def get_locator_by_xpath(self, selector):
        # div[@class="et_pb_button_wrapper"]
        # //*[@id='button1']
        xpath = (By.XPATH, selector)
        return self.browser.find_element(*xpath)

    def get_locator_by_id(self, selector):
        id = (By.ID, selector)
        return self.browser.find_element(*id)

    def get_locator_by_slass_name(self, selector):
        # class_name
        class_name = (By.CLASS_NAME, selector)
        return self.browser.find_element(*class_name)

    def get_locator_by_contains(self, selector):
        # //div[contains(@class,"et_pb_module")]
        xpath = (By.XPATH, f'//div[contains(@class,"{selector}")]')
        return self.browser.find_element(*xpath)

    def get_locator_by_contains_text(self, text):
        # // *[contains(text(), "Click Me")]
        xpath = (By.XPATH, f'// *[contains(text(),"{text}")]')
        return self.browser.find_element(*xpath)

    def click(self, selector, by="css"):
        locator = self.get_element(selector)
        self.browser.execute_script("arguments[0].scrollIntoView();", locator)
        locator.click()
        return locator
    def click_xpath(self, selector):
        locator = self.get_element_xpath(selector)
        self.browser.execute_script("arguments[0].scrollIntoView();", locator)
        locator.click()
        return locator
    def get_element_xpath(self, selector):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def get_element(self, selector):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def assert_that_element_is_selected(self, selector):
        return self.get_locator_by_css(selector).is_selected()

    def assert_that_element_is_selected_xpath(self, selector):
        return self.get_locator_by_xpath(selector).is_selected()

    def assert_that_element_is_not_selected_xpath(self, selector):
        return self.get_locator_by_xpath(selector).is_selected() == False

    def open_iframe(self, locator):
        return self.browser.switch_to.frame(self.browser.find_element(By.XPATH, locator))

    def scroll_to_xpath(self, selector):
        locator = self.get_element_xpath(selector)
        self.browser.execute_script("arguments[0].scrollIntoView();", locator)
        return locator

    def select_value_from_dropdown(self, value):
        element = self.get_locator_by_xpath(value)
        element.click()

    def get_text(self, selector):
        return self.get_locator_by_xpath(selector).text