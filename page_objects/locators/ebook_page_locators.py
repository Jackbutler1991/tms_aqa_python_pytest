from page_objects.locators.base_locators import get_locator_by_id


class EbookPageLocators():
    # Sing_In_Locators
    NASA_TO_NOW_BOOK = get_locator_by_id('"ember151"]/div')
    NASA_TO_NOW_BOOK_PDF = get_locator_by_id('"ember23"]//p[6]')