from pages.product_page import ProductPage

# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    book_name = page.get_book_name()
    price = page.get_price()
    page.should_be_book_name_the_same_in_basket(book_name)
    page.should_be_price_the_same_in_basket(price)