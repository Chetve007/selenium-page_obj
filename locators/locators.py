from selenium.webdriver.common.by import By


class MainPageLocators:
    pass
    # LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    # Log in
    EMAIL_ADDR = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOG_IN_BTN = (By.NAME, 'login_submit')

    # Register
    EMAIL_ADDR_REG = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REG = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASS = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BTN = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alert-info strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, 'span a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET = (By.CSS_SELECTOR, 'div.page-header h1')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, '#content_inner h2.col-sm-6')
