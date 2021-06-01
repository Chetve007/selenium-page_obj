from locators.locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_book_name_the_same_in_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text
        assert book_name == book_name_in_basket

    def should_be_price_the_same_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price == price_in_basket
