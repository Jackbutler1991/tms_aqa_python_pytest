from base_page import BasePage

class NasaPage(BasePage):
    LOGO = '//*[@id="navbar-nasa"]//img'
    MENU_MISSION = '//*[@id="nasa-main-menu"]/li[2]//span[1]'
    NEWS_BLOCK_1 = '//*[@id="ember33"]/div'
    YOUTUBE_VIDEO = 'ytp-cued-thumbnail-overlay-image'
