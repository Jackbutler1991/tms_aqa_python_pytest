from locators.BaseLocators import get_locator_by_id
from elements.element import Element
class ContainerLocators():
    LOGO_ver2 = Element(get_locator_by_id('"navbar-nasa"]//img'))
    LOGO = get_locator_by_id('"navbar-nasa"]//img')

    #HEADER
    SEARCH = get_locator_by_id('"ember26"]')
    SEARCH_INPUT = get_locator_by_id('"ember22"]')
    SEARCH_BUTTON = get_locator_by_id('"ember25"]')
    SEARCH_MOON = get_locator_by_id('"news-items"]//h3')
    SEARCH_NO_RESULT = get_locator_by_id('"no-results"]/div')

    HEAD_MISSIONS = get_locator_by_id('"nasa-main-menu"]/li[2]//span[1]')
    HEAD_MISSIONS_DROPDOWN_OPEN = get_locator_by_id('"nasa-main-menu"]/li[2]')

    HEAD_GALLERIES = get_locator_by_id('"nasa-main-menu"]/li[3]//span[1]')
    HEAD_GALLERIES_DROPDOWN_OPEN = get_locator_by_id('"nasa-main-menu"]/li[3]')

    HUMANS_IN_SPACE = get_locator_by_id('"nasa-main-menu"]/li[1]//li[1]/a')

    FLIGHT = get_locator_by_id('"nasa-main-menu"]/li[1]//li[5]/a')
    SOLAR_SUSTEM = get_locator_by_id('"nasa-main-menu"]/li[1]//li[6]/a')
    STEM_ENGAGEMENT = get_locator_by_id('"nasa-main-menu"]/li[1]//li[7]/a')

    #BODY
    BG_CARD_CANVAS = get_locator_by_id('"ember166"]/div')
    NASA_EVENTS_CARD = get_locator_by_id('"cards"]/div[1]/div')
    TEXT_NASA_EVENTS = get_locator_by_id('"cards"]/div[1]//h2')
    TEXT_NASA_TV_SCHEDULE = get_locator_by_id('"cards"]//div[6]/a[1]')
    TEXT_NASA_LAUNCHES = get_locator_by_id('"cards"]//div[6]/a[2]')

    #FOOTER
    TEXT_IN_FOOTER1 = get_locator_by_id('"status"]/span[1]')

    #Sing In
    PALL_LOGIN_USER_NAME = ('uxUserName]')
    PALL_LOGIN_PASSWORD = ('"uxPassword"]')
    SIGN_IN_BUTTON = get_locator_by_id('"ContentPlaceHolder1_uxLogin"]')
    SING_IN_SUCCESSFUL = get_locator_by_id('"wraper"]//strong')

    #Sing_In_Data
    TEST_PASSWORD_1 = ('qwrqwr')
    TEST_LOGIN_1 = ('asdsa123')
    TEST_PASSWORD = ('83BYqe_+')
    TEST_LOGIN = ('AlexanderParniushka')
    SUCSESFFUL_LOGIN = ('"wraper"]//font/font/font')

