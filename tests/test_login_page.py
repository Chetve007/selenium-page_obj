from pages.login_page import LoginPage

LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


def test_go_to_login_page(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_login_page()
