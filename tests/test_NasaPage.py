import allure

from page_elements.container import ContainerElement

@allure.story('Тест Nasa')
@allure.title('Тест отображения логотипа')
def test_logo(browser, open_page):
    container = ContainerElement(browser)
    container.asser_that_logo_visible()

def test_logo_ver2(browser, open_page):
    container = ContainerElement(browser)
    container.asser_that_logo_visible_ver2()

#HEADER_NASA_GOV
def test_head_menu_missions(browser, open_page):
    container = ContainerElement(browser)
    browser.fullscreen_window()
    container.click_head_menu_missions()
    container.is_displayed_menu_missions()

def test_head_menu_galleries(browser, open_page):
    container = ContainerElement(browser)
    browser.fullscreen_window()
    container.click_head_menu_galleries()
    container.is_displayed_menu_galleries()

def test_head_menu_humans_in_space(browser, open_page):
    container = ContainerElement(browser)
    browser.fullscreen_window()
    container.click_head_menu_humans_in_space()
    container.check_open_page_humans_in_space()

def test_singin_fqia(browser, open_page):
    container = ContainerElement(browser)
    container.singin_fqia()
    container.click_head_menu_humans_in()
