import allure
from page_objects.pages.nasa_gov import NasaPage
from page_objects.pages.search_page import Search
from page_objects.pages.sign_in_page import SignIn
from page_objects.pages.ebook_page import EbookPage


@allure.suite("Nasa Page")
class TestNasaPage:
    # HEADER_NASA_PAGE
    @allure.title("Nasa Page header Test: open menu missions")
    def test_head_menu_missions(self, browser, open_page):
        menu_missions = NasaPage(browser)
        browser.fullscreen_window()
        menu_missions.click_head_menu_missions()
        menu_missions.assert_is_displayed_menu_missions()

    @allure.title("Nasa Page header Test: open menu galleries")
    def test_head_menu_galleries(self, browser, open_page):
        menu_galleries = NasaPage(browser)
        browser.fullscreen_window()
        menu_galleries.click_head_menu_galleries()
        menu_galleries.assert_is_displayed_menu_galleries()

    @allure.title("Nasa Page header Test: open menu humans in space")
    def test_head_menu_humans_in_space(self, browser, open_page):
        human_in_space = NasaPage(browser)
        browser.fullscreen_window()
        human_in_space.click_head_menu_humans_in_space()
        human_in_space.check_open_page_humans_in_space()

    # BODY_NASA_PAGE
    @allure.title("Nasa Page Test: check logo")
    def test_logo(self, browser, open_page):
        test_logo = NasaPage(browser)
        test_logo.assert_that_logo_visible()

    @allure.title("Nasa Page Test: check select from follow Nasa")
    def test_choose_follow_from_cat(self, browser, open_page):
        choose_follow_nasa = NasaPage(browser)
        choose_follow_nasa.find_categories()
        choose_follow_nasa.click_follow_nasa()
        choose_follow_nasa.asser_change_main_page_url()

    @allure.title("Nasa Page Test: check big news banner")
    def test_bg_card_canvas_is_visible(self, browser, open_page):
        big_card_visible = NasaPage(browser)
        big_card_visible.bg_card_canvas_is_visible()

    @allure.title("Nasa Page Test: check small news banner")
    def test_event_cards_is_visible(self, browser, open_page):
        event_card = NasaPage(browser)
        event_card.event_cards_is_visible()

    @allure.title("Nasa Page Test: check text in nasa events")
    def test_text_nasa_events(self, browser, open_page):
        nasa_events_text = NasaPage(browser)
        nasa_events_text.check_text_nasa_events()

    @allure.title("Nasa Page Test: click learn where to look")
    def test_choose_developer_from_categories(self, browser, open_page):
        click_learn_where = NasaPage(browser)
        click_learn_where.find_categories()
        click_learn_where.click_learn_where()
        click_learn_where.asser_change_main_page_url()

    @allure.title("Nasa Page Test: check text in nasa tv shedule")
    def test_text_nasa_tv_shedule(self, browser, open_page):
        nasa_tv_shedule = NasaPage(browser)
        nasa_tv_shedule.text_nasa_tv_shedule()

    @allure.title("Nasa Page Test: check text in nasa launches")
    def test_text_nasa_launches(self, browser, open_page):
        nasa_launches = NasaPage(browser)
        nasa_launches.check_text_nasa_launches()

    @allure.title("Nasa Page Test: open flight page")
    def test_open_flight_page(self, browser, open_page):
        flight_page = NasaPage(browser)
        browser.fullscreen_window()
        flight_page.open_flight_page()

    @allure.title("Nasa Page Test: click live iss")
    def test_choose_live_iss_from_cat(self, browser, open_page):
        click_live_iss = NasaPage(browser)
        click_live_iss.find_categories()
        click_live_iss.click_live_iss()
        click_live_iss.asser_change_main_page_url()

    @allure.title("Nasa Page Test: open solar system page")
    def test_open_solar_system_page(self, browser, open_page):
        solar_system_page = NasaPage(browser)
        browser.fullscreen_window()
        solar_system_page.open_flight_page()
        solar_system_page.chek_open_flight_page()

    @allure.title("Nasa Page Test: open engagement page")
    def test_open_stem_engagement(self, browser, open_page):
        stem_engagement = NasaPage(browser)
        browser.fullscreen_window()
        stem_engagement.open_stem_engagement_page()
        stem_engagement.check_open_stem_engagement_page()

    @allure.title("Nasa Page Test: click see all faqs")
    def test_choose_dev_from_categories(self, browser, open_page):
        click_see_all_faqs = NasaPage(browser)
        click_see_all_faqs.find_categories()
        click_see_all_faqs.click_see_all_faqs()
        click_see_all_faqs.asser_change_main_page_url()

    # FOOTER_NASA_PAGE
    @allure.title("Nasa Page footer Test: chek text")
    def test_text_in_footer(self, browser, open_page):
        footer_text = NasaPage(browser)
        footer_text.check_elem()

    @allure.title("Nasa Page footer Test: open privacy page")
    def test_open_privacy_in_footer(self, browser, open_page):
        privacy_page = NasaPage(browser)
        browser.fullscreen_window()
        privacy_page.open_privacy_page()
        privacy_page.check_open_privacy_page()

    @allure.title("Nasa Page footer Test: open accessability page")
    def test_open_accessability_in_footer(self, browser, open_page):
        accessability_page = NasaPage(browser)
        browser.fullscreen_window()
        accessability_page.open_accessability_page()
        accessability_page.check_open_accessability_page()

    @allure.title("Nasa Page footer Test: open counsel page")
    def test_open_special_counsel_in_footer(self, browser, open_page):
        counsel_page = NasaPage(browser)
        browser.fullscreen_window()
        counsel_page.open_special_counsel_page()
        counsel_page.check_open_special_counsel_page()


@allure.suite("Ebook Page")
class TestEbookPage:
    # HEADER_EBOOK_PAGE
    @allure.title("Ebook Page Test: open nasa book")
    def test_open_nasa_ebook_pdf(self, browser, open_ebook_page):
        open_ebook_pdf = EbookPage(browser)
        open_ebook_pdf.click_to_open_nasa_book_page()
        open_ebook_pdf.click_to_open_nasa_book_pdf()
        open_ebook_pdf.assert_if_pdf_nasa_book_open()

    @allure.title("Ebook Page Test: open The wind book")
    def test_open_the_wind_ebook_epub(self, browser, open_ebook_page):
        open_ebook_upub = EbookPage(browser)
        open_ebook_upub.click_to_open_the_wind_book_page()
        open_ebook_upub.click_to_open_the_wind_book_pdf()
        open_ebook_upub.assert_if_pdf_the_wind_book_open()

    @allure.title("Ebook Page Test: open More Stories")
    def test_click_more_stories(self, browser, open_ebook_page):
        more_stories = EbookPage(browser)
        more_stories.click_more_stories()
        more_stories.scroll_to_last_book()
        more_stories.assert_open_more_book()

    @allure.title("Ebook Page Test: check click Accessibility on footer")
    def test_click_asessibility(self, browser, open_ebook_page):
        accessibility_footer = EbookPage(browser)
        accessibility_footer.scroll_to_ebook_footer()
        accessibility_footer.click_accessibility_footer()
        accessibility_footer.assert_accessibility_is_displayed()

    @allure.title("Ebook Page Test: click on logo footer")
    def test_logo_logo_is_displayed_footer(self, browser, open_ebook_page):
        click_logo_footer = EbookPage(browser)
        click_logo_footer.scroll_to_footer()
        click_logo_footer.check_logo_is_displayed()

    @allure.title("Ebook Page Test: check logo footer is displayed")
    def test_click_logo_in_footer(self, browser, open_ebook_page):
        logo_footer_displayed = EbookPage(browser)
        logo_footer_displayed.scroll_to_footer()
        logo_footer_displayed.click_logo_footer()
        logo_footer_displayed.check_url()


@allure.suite("Search")
class TestSearch:
    @allure.title("Nasa Page Test: check search field")
    def test_search_is_visible(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_is_visible()

    @allure.title("Nasa Page Test: check search (valid data)")
    def test_search_input_moon(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_input()
        search_test.search_click()
        search_test.check_search_moon()

    @allure.title("Nasa Page Test: check search (special characters)")
    def test_search_input_special(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_input_special()
        search_test.search_click()
        search_test.check_search_special()

    @allure.title("Nasa Page Test: check "
                  "search (special characters) and push enter")
    def test_search_input_special_enter(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_input_special()
        search_test.enter()
        search_test.check_search_special()

    @allure.title("Nasa Page Test: check search (one symbol)")
    def test_search_input_one_symbol(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_input_one_symbol()
        search_test.search_click()
        search_test.check_search_one_symbol()

    @allure.title("Nasa Page Test: check search (one symbol) and push enter")
    def test_search_input_one_symbol_enter(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_input_one_symbol()
        search_test.enter()
        search_test.check_search_one_symbol()

    @allure.title("Nasa Page Test: check search (more 255 symbols)")
    def test_search_input_more_255_symbols(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_input_more255_symbol()
        search_test.search_click()
        search_test.check_search_more255_symbol()

    @allure.title("Nasa Page Test: check search"
                  " (more 255 symbols) and push enter")
    def test_search_input_more_255_symbols_enter(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_input_more255_symbol()
        search_test.enter()
        search_test.check_search_more255_symbol()

    @allure.title("Nasa Page Test: check search (another language)")
    def test_search_input_another_language(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_input_another_language()
        search_test.search_click()
        search_test.check_search_another_language()

    @allure.title("Nasa Page Test: check search"
                  " (another language) and push enter")
    def test_search_input_another_language_enter(self, browser, open_page):
        search_test = Search(browser)
        search_test.search_input_another_language()
        search_test.enter()
        search_test.check_search_another_language()


@allure.suite("Sign in page")
class TestSignIn:
    @allure.title("Freedom of Information Act Page Test: check sign in")
    def test_singin_freedom_of_information(self, browser, open_page):
        sing_in = SignIn(browser)
        sing_in.singin_freedom_of_information()
        sing_in.click_head_menu_humans_in()
        sing_in.check_in_sucsessfull()

    @allure.title("Freedom of Information Act Page Test: check sign in (neg)")
    def test_singin_freedom_of_inf_wrong_data(self, browser, open_page):
        sing_in = SignIn(browser)
        sing_in.singin_freedom_of_information_neg1()
        sing_in.click_head_menu_humans_in()

    @allure.title("Freedom of Information "
                  "Act Page Test: check sign in (empty field)")
    def test_singin_freedom_of_inf_empty_fields(self, browser, open_page):
        sing_in = SignIn(browser)
        sing_in.singin_freedom_of_information_neg2()
        sing_in.click_head_menu_humans_in()
