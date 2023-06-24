import allure
from page_elements.container import ContainerElement


@allure.suite("Nasa Page")
class TestNasaPage:
    #BODY_NASA_PAGE
    @allure.title("Nasa Page Test: check logo")
    def test_logo(self, browser, open_page):
        container = ContainerElement(browser)
        container.asser_that_logo_visible()


    @allure.title("Nasa Page Test: check search field")
    def test_search_is_visible(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_is_visible()


    @allure.title('Тест отображения большой карточки новостей')
    def test_bg_card_canvas_is_visible(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_is_visible()


    @allure.title('Тест отображения второй маленькой карточки новостей')
    def test_event_cards_is_visible(self, browser, open_page):
        container = ContainerElement(browser)
        container.event_cards_is_visible()


    # HEADER_NASA_GOV
    @allure.title('Тест раскрытия меню миссий')
    def test_head_menu_missions(self, browser, open_page):
        container = ContainerElement(browser)
        browser.fullscreen_window()
        container.click_head_menu_missions()
        container.is_displayed_menu_missions()


    @allure.title('Тест раскрытия меню галереи')
    def test_head_menu_galleries(self, browser, open_page):
        container = ContainerElement(browser)
        browser.fullscreen_window()
        container.click_head_menu_galleries()
        container.is_displayed_menu_galleries()


    @allure.title('Тест раскрытия меню "люди в космосе"')
    def test_head_menu_humans_in_space(self, browser, open_page):
        container = ContainerElement(browser)
        browser.fullscreen_window()
        container.click_head_menu_humans_in_space()
        container.check_open_page_humans_in_space()


    @allure.title('Тест отображения логотипа.2')
    def test_logo_ver2(self, browser, open_page):
        container = ContainerElement(browser)
        container.asser_that_logo_visible_ver2()


    # FOOTER_NASA_GOV
    @allure.title('Тест отображения текста в футере')
    def test_text_in_footer(self, browser, open_page):
        container = ContainerElement(browser)
        container.check_elem()


    @allure.title('Тест открытия страницы "Privacy" в футере')
    def test_open_privacy_in_footer(self, browser, open_page):
        container = ContainerElement(browser)
        browser.fullscreen_window()
        container.open_privacy_page()


    @allure.title('Тест открытия страницы "Accessability" в футере')
    def test_open_accessability_in_footer(self, browser, open_page):
        container = ContainerElement(browser)
        browser.fullscreen_window()
        container.open_accessability_page()


    @allure.title('Тест открытия страницы "Special Counsel" в футере')
    def test_open_special_counsel_in_footer(self, browser, open_page):
        container = ContainerElement(browser)
        browser.fullscreen_window()
        container.open_special_counsel_page()


    # BODY_NASA_GOV
    @allure.title('Тест отображения текста в блоке "События"')
    def test_text_nasa_events(self, browser, open_page):
        container = ContainerElement(browser)
        container.text_nasa_events()


    @allure.title('Тест отображения текста в блоке "График событий"')
    def test_text_nasa_tv_shedule(self, browser, open_page):
        container = ContainerElement(browser)
        container.text_nasa_tv_shedule()


    @allure.title('Тест отображения текста в блоке "Запуски"')
    def test_text_nasa_launches(self, browser, open_page):
        container = ContainerElement(browser)
        container.text_nasa_launches()


    @allure.title('Тест входа в аккаунт')
    def test_singin_fqia(self, browser, open_page):
        container = ContainerElement(browser)
        container.singin_fqia()
        container.click_head_menu_humans_in()
        container.check_in_sucsessfull()


    @allure.title('Тест входа в аккаунт (ввод невалидных данных)')
    def test_singin_fqia_wrong_data(self, browser, open_page):
        container = ContainerElement(browser)
        container.singin_fqia_neg1()
        container.click_head_menu_humans_in()


    @allure.title('Тест входа в аккаунт (пустые поля)')
    def test_singin_fqia_empty_fields(self, browser, open_page):
        container = ContainerElement(browser)
        container.singin_fqia_neg2()
        container.click_head_menu_humans_in()
    #    container.test_test()


    @allure.title('Тест открытия страницы "полеты"')
    def test_open_flight_page(self, browser, open_page):
        container = ContainerElement(browser)
        browser.fullscreen_window()
        container.open_flight_page()


    @allure.title('Тест открытия страницы "солнечной системы"')
    def test_open_solar_system_page(self, browser, open_page):
        container = ContainerElement(browser)
        browser.fullscreen_window()
        container.open_flight_page()


    @allure.title('Тест открытия страницы "обязательства"')
    def test_open_stem_engagement(self, browser, open_page):
        container = ContainerElement(browser)
        browser.fullscreen_window()
        container.open_stem_engagement_page()


    @allure.title('Тест поиска по сайту с вводом валидных данных')
    def test_search_input_moon(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_input()
        container.search_click()
        container.text_search_moon()


    @allure.title('Тест поика по сайту, ввод спец символов')
    def test_search_input_special(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_input_special()
        container.search_click()
        container.text_search_special()


    @allure.title('Тест поика по сайту, ввод спец символов (нажатие ENTER)')
    def test_search_input_special_enter(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_input_special()
        container.enter()
        container.text_search_special()


    @allure.title('Тест поика по сайту, ввод одного символа')
    def test_search_input_one_symbol(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_input_one_symbol()
        container.search_click()
        container.text_search_one_symbol()


    @allure.title('Тест поика по сайту, ввод одного символа (нажатие ENTER)')
    def test_search_input_one_symbol_enter(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_input_one_symbol()
        container.enter()
        container.text_search_one_symbol()


    @allure.title('Тест поика по сайту, ввод спец символов')
    def test_search_input_more_255_symbols(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_input_more255_symbol()
        container.search_click()
        container.text_search_more255_symbol()


    @allure.title('Тест поика по сайту, ввод спец символов (нажатие ENTER)')
    def test_search_input_more_255_symbols_enter(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_input_more255_symbol()
        container.enter()
        container.text_search_more255_symbol()


    @allure.title('Тест поика по сайту, ввод кириллицы')
    def test_search_input_another_language(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_input_another_language()
        container.search_click()
        container.text_search_another_language()


    @allure.title('Тест поика по сайту, ввод кириллицы (нажатие ENTER)')
    def test_search_input_another_language_enter(self, browser, open_page):
        container = ContainerElement(browser)
        container.search_input_another_language()
        container.enter()
        container.text_search_another_language()
