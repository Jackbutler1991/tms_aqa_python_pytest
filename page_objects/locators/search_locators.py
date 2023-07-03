from page_objects.locators.base_locators import get_locator_by_id


class SearchLocators():
    # Search_locators
    SEARCH = get_locator_by_id('"ember20"]')
    SEARCH_INPUT = get_locator_by_id('"ember20"]')
    SEARCH_BUTTON = get_locator_by_id('"ember23"]')
    SEARCH_MOON = get_locator_by_id('"news-items"]//h3')
    SEARCH_NO_RESULT = get_locator_by_id('"no-results"]/div')

    # Search_data
    SEARCH_MORE255_SYMBOLS = ('12345678910123456789101234567891012345678910'
                              '12345678910123456789101234567891012345678910'
                              '12345678910123456789101234567891012345678910'
                              '12345678910123456789101234567891012345678910'
                              '12345678910123456789101234567891012345678910'
                              '12345678910123456789101234567891012345678910'
                              '12345678910123456789101')
