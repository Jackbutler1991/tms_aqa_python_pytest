import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    driver.implicitly_wait(10)

    yield driver

    driver.close()
    driver.quit()
