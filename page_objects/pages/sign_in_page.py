import allure
from selenium.webdriver.common.by import By
from page_objects.pages.base_page import BasePage
from page_objects.locators.sign_in_locators import SignInLocators
from page_objects.locators.sign_in_data import SignInData


class SignIn(BasePage, SignInLocators):
    def __init__(self, browser):
        super().__init__(browser)
        self.locator = SignInLocators()
        self.data = SignInData()

    @allure.step("singin to freedom of information")
    def singin_freedom_of_information(self):
        self.browser.get('https://pal.hq.nasa.gov/app/PalLogin.aspx')
        self.browser.find_element(By.XPATH, '//*[@id="uxUserName"]').send_keys(self.data.TEST_LOGIN)
        self.browser.find_element(By.XPATH, '//*[@id="uxPassword"]').send_keys(self.data.TEST_PASSWORD)

    @allure.step("singin to freedom of information, negative")
    def singin_freedom_of_information_neg1(self):
        self.browser.get('https://pal.hq.nasa.gov/app/PalLogin.aspx')
        self.browser.find_element(By.XPATH, '//*[@id="uxUserName"]').send_keys(self.data.TEST_LOGIN_1)
        self.browser.find_element(By.XPATH, '//*[@id="uxPassword"]').send_keys(self.data.TEST_PASSWORD_1)

    @allure.step("singin to freedom of information, empty field")
    def singin_freedom_of_information_neg2(self):
        self.browser.get('https://pal.hq.nasa.gov/app/PalLogin.aspx')

    @allure.step("click on the head menu human in")
    def click_head_menu_humans_in(self):
        self.click_xpath(self.locator.SIGN_IN_BUTTON)

    @allure.step("check if sign ib is successful")
    def check_in_sucsessfull(self):
        text_element = self.check_text_by_xpath(self.locator.SING_IN_SUCCESSFUL)
        print(text_element)
        assert text_element == "Sign in Successful."
