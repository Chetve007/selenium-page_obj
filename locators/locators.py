from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


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
