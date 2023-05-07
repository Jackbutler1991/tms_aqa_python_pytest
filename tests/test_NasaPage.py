from page_elements.container import ContainerElement

def test_logo(browser, open_page):
    container = ContainerElement(browser)
    container.asser_that_logo_visible()


def test_logo_ver2(browser, open_page):
    container = ContainerElement(browser)
    container.asser_that_logo_visible_ver2()