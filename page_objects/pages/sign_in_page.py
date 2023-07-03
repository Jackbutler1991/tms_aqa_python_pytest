from selenium.webdriver.common.by import By
from base_page import BasePage
from page_objects.locators.sign_in_locators import SignInLocators


class SignIn(BasePage, SignInLocators):
    def __init__(self, browser):
        super().__init__(browser)
        self.locator = SignInLocators()

    def singin_freedom_of_information(self):
        self.browser.get('https://pal.hq.nasa.gov/app/PalLogin.aspx')
        self.browser.find_element(By.XPATH, '//*[@id="uxUserName"]').send_keys(self.TEST_LOGIN)
        self.browser.find_element(By.XPATH, '//*[@id="uxPassword"]').send_keys(self.TEST_PASSWORD)

    def singin_freedom_of_information_neg1(self):
        self.browser.get('https://pal.hq.nasa.gov/app/PalLogin.aspx')
        self.browser.find_element(By.XPATH, '//*[@id="uxUserName"]').send_keys(self.TEST_LOGIN_1)
        self.browser.find_element(By.XPATH, '//*[@id="uxPassword"]').send_keys(self.TEST_PASSWORD_1)

    def singin_freedom_of_information_neg2(self):
        self.browser.get('https://pal.hq.nasa.gov/app/PalLogin.aspx')

    def click_head_menu_humans_in(self):
        self.click_xpath(self.locator.SIGN_IN_BUTTON)

    def check_in_sucsessfull(self):
        text_element = self.check_text_by_xpath(self.locator.SING_IN_SUCCESSFUL)
        print(text_element)
        assert text_element == "Sign in Successful."
