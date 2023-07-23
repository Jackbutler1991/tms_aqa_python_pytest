import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.core.utils import ChromeType


@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    driver.implicitly_wait(10)

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture
def open_page(browser):
    browser.get('https://www.nasa.gov/')
    browser.fullscreen_window()

@pytest.fixture
def open_ebook_page(browser):
    browser.get('https://www.nasa.gov/connect/ebooks/index.html')
    browser.fullscreen_window()


@pytest.fixture
def open_no_fear_act_page(browser):
    browser.get(
        "https://www.nasa.gov/offices/odeo/no-fear-act"
    )
    browser.fullscreen_window()


@pytest.fixture
def open_freedom_of_information_act_page(browser):
    browser.get(
        "https://www.nasa.gov/FOIA/index.html"
    )
    browser.fullscreen_window()


@pytest.fixture
def open_sign_in_page(browser):
    browser.get(
        "https://pal.hq.nasa.gov/"
    )
    browser.fullscreen_window()
