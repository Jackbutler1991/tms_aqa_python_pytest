from page_objects.locators.base_locators import get_locator_by_id


class ContainerLocators():
    # HEADER
    HEAD_MISSIONS = get_locator_by_id('"nasa-main-menu"]/li[2]//span[1]')
    HEAD_MISSIONS_DROPDOWN_OPEN = get_locator_by_id('"nasa-main-menu"]/li[2]')

    HEAD_GALLERIES = get_locator_by_id('"nasa-main-menu"]/li[3]//span[1]')
    HEAD_GALLERIES_DROPDOWN_OPEN = get_locator_by_id('"nasa-main-menu"]/li[3]')

    HUMANS_IN_SPACE = get_locator_by_id('"nasa-main-menu"]/li[1]//li[1]/a')

    FLIGHT = get_locator_by_id('"nasa-main-menu"]/li[1]//li[5]/a')
    SOLAR_SUSTEM = get_locator_by_id('"nasa-main-menu"]/li[1]//li[6]/a')
    STEM_ENGAGEMENT = get_locator_by_id('"nasa-main-menu"]/li[1]//li[7]/a')

    LOGO = get_locator_by_id('"navbar-nasa"]//img')

    FOLLOW_NASA_CATEGORIES = get_locator_by_id('"nasa-main-menu"]/li[5]//span[1]')
    FOLLOW_NASA_SPOT_STATION = get_locator_by_id('"nasa-main-menu"]/li[5]//li[7]/a')
    LEARN_WHERE_TO_LOOK = ('//div[5]/div[1]/div[2]//a')
    LIVE_ISS = ('//div[3]/div[1]/div[2]//a')
    SEE_ALL_FAQS = ('//div[4]/div[1]/div[2]//a')


    # BODY
    BG_CARD_CANVAS = get_locator_by_id('"ember166"]/div')
    NASA_EVENTS_CARD = get_locator_by_id('"cards"]/div[1]/div')
    TEXT_NASA_EVENTS = get_locator_by_id('"cards"]/div[1]//h2')
    TEXT_NASA_TV_SCHEDULE = get_locator_by_id('"cards"]//div[6]/a[1]')
    TEXT_NASA_LAUNCHES = get_locator_by_id('"cards"]//div[6]/a[2]')

    # FOOTER
    TEXT_IN_FOOTER1 = get_locator_by_id('"status"]/span[1]')
    PRIVACY = get_locator_by_id('"footer-links"]/li[3]/a')
    ACCESSIBILITY = get_locator_by_id('"footer-links"]/li[4]/a')
    SPECIAL_COUNSEL = get_locator_by_id('"footer-links"]/li[6]/a')
