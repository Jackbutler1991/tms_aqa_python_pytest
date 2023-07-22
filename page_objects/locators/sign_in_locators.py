from page_objects.locators.base_locators import get_locator_by_id


class SignInLocators():
    # Sing_In_Locators
    SIGN_IN_BUTTON = get_locator_by_id('"ContentPlaceHolder1_uxLogin"]')
    SING_IN_SUCCESSFUL = get_locator_by_id('"wraper"]//strong')


