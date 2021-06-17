from locators.locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def go_to_login_page(self):                   перенесли в base_page.py
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click()

        # alert = self.browser.switch_to.alert
        # alert.accept()

        # return LoginPage(browser=self.browser, url=self.browser.current_url)  # 1 approach: init another page in current page

    # def should_be_login_link(self):                    перенесли в base_page.py
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'
