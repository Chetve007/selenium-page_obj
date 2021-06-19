from locators.locators import BasketPageLocators
from pages.base_page import BasePage


class BasketPage(BasePage):

    def should_be_basket_page(self):
        assert 'Basket' in self.browser.find_element(*BasketPageLocators.BASKET).text, 'Basket is not presented'

    def basket_should_be_empty(self):
        assert 'Your basket is empty.' in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text, \
            'Basket is not empty'

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
            'Basket is not empty'
