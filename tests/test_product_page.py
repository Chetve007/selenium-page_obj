import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
LINK_WITHOUT_PROMO = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
NEW_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
LINK_BE = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    book_name = page.get_book_name()
    price = page.get_price()
    page.should_be_book_name_the_same_in_basket(book_name)
    page.should_be_price_the_same_in_basket(price)


@pytest.mark.parametrize('promo',
                         [pytest.param(item, marks=pytest.mark.xfail(item == 7, reason='Bad promo'))
                          for item in range(10)])
def test_guest_can_add_product_to_basket_params(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    book_name = page.get_book_name()
    price = page.get_price()
    page.should_be_book_name_the_same_in_basket(book_name)
    page.should_be_price_the_same_in_basket(price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK_WITHOUT_PROMO)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK_WITHOUT_PROMO)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, NEW_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, NEW_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK_BE)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.basket_should_be_empty()
    basket_page.should_not_be_goods_in_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

        email = f'{time.time()}_@fakemail.ru'

        login_page.register_new_user(email, 'pass12345')
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK_WITHOUT_PROMO)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        book_name = page.get_book_name()
        price = page.get_price()
        page.should_be_book_name_the_same_in_basket(book_name)
        page.should_be_price_the_same_in_basket(price)
