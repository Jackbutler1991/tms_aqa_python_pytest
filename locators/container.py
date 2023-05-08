from locators.BaseLocators import get_locator_by_id
from elements.element import Element
class ContainerLocators():
    LOGO_ver2 = Element(get_locator_by_id('"navbar-nasa"]//img'))
    LOGO = get_locator_by_id('"navbar-nasa"]//img')

    HEAD_MISSIONS = get_locator_by_id('"nasa-main-menu"]/li[2]/a/span[1]')
    HEAD_MISSIONS_DROPDOWN_OPEN = ('//*[@id="nasa-main-menu"]/li[2]')









#   LOGO = self.Get_locator.get_locator_by_xpath('//*[@id="navbar-nasa"]//img')
#    MENU_MISSION = '//*[@id="nasa-main-menu"]/li[2]//span[1]'
#    NEWS_BLOCK_1 = '//*[@id="ember33"]/div'
#    YOUTUBE_VIDEO = 'ytp-cued-thumbnail-overlay-image'