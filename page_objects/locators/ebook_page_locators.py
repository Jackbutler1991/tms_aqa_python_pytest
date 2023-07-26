from page_objects.locators.base_locators import get_locator_by_id


class EbookPageLocators():
    # Ebook_Locators
    NASA_TO_NOW_BOOK = get_locator_by_id('"ember151"]/div')
    NASA_TO_NOW_BOOK_PDF = get_locator_by_id('"ember23"]//p[6]')
    THE_WIND_BOOK_PAGE = get_locator_by_id('"ember187"]/div')
    THE_WIND_BOOK_PDF = get_locator_by_id('"ember187"]/div')
    MORE_STORIES = get_locator_by_id('"trending"]')
    PROBING_THE_SKY = get_locator_by_id('"ember428"]/div')
    ACCESSIBILITY_FOOTER = get_locator_by_id('footer-links"]/li[4]/a')
    LOGO_FOOTER = get_locator_by_id('"footer-info"]/a/img')