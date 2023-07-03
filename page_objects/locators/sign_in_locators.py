from page_objects.locators.base_locators import get_locator_by_id


class SignInLocators():
    # Sing_In_Locators
    PALL_LOGIN_USER_NAME = ('uxUserName]')
    PALL_LOGIN_PASSWORD = ('"uxPassword"]')

    SIGN_IN_BUTTON = get_locator_by_id('"ContentPlaceHolder1_uxLogin"]')
    SING_IN_SUCCESSFUL = get_locator_by_id('"wraper"]//strong')

    # Sing_In_Data
    TEST_PASSWORD_1 = ('qwrqwr')
    TEST_LOGIN_1 = ('asdsa123')
    TEST_PASSWORD = ('83BYqe_+')
    TEST_LOGIN = ('AlexanderParniushka')
    SUCCESSFUL_LOGIN = ('"wraper"]//font/font/font')
