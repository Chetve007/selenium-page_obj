from locators.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_BTN), 'Log in widget is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), 'Register widget is not presented'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_ADDR_REG).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REG).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()
