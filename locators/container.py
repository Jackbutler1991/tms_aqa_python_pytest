from locators.BaseLocators import get_locator_by_id
from elements.element import Element
class ContainerLocators():
    LOGO_ver2 = Element(get_locator_by_id('"navbar-nasa"]//img'))
    LOGO = get_locator_by_id('"navbar-nasa"]//img')

    #HEADER
    HEAD_MISSIONS = get_locator_by_id('"nasa-main-menu"]/li[2]//span[1]')
    HEAD_MISSIONS_DROPDOWN_OPEN = get_locator_by_id('"nasa-main-menu"]/li[2]')

    HEAD_GALLERIES = get_locator_by_id('"nasa-main-menu"]/li[3]//span[1]')
    HEAD_GALLERIES_DROPDOWN_OPEN = get_locator_by_id('"nasa-main-menu"]/li[3]')

    HUMANS_IN_SPACE = get_locator_by_id('"nasa-main-menu"]/li[1]//li[1]/a')

    #Sing In
    PALL_LOGIN_USER_NAME = ('uxUserName]')
    PALL_LOGIN_PASSWORD = ('"uxPassword"]')
    SIGN_IN_BUTTON = get_locator_by_id('"ContentPlaceHolder1_uxLogin"]')




