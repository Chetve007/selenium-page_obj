from pages.product_page import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_book_name_the_same_in_basket()
    page.should_be_price_the_same_in_basket()
