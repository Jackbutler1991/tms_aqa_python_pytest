from page_objects.locators.base_locators import get_locator_by_id


class SearchLocators():
    # Search_locators
    SEARCH = get_locator_by_id('"ember20"]')
    SEARCH_INPUT = get_locator_by_id('"ember20"]')
    SEARCH_BUTTON = get_locator_by_id('"ember23"]')
    SEARCH_MOON = get_locator_by_id('"news-items"]//h3')
    SEARCH_NO_RESULT = get_locator_by_id('"no-results"]/div')
