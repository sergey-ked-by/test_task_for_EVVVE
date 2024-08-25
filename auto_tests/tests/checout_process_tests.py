from auto_tests.utils.ui_helpers import login, search_product, add_product_to_cart, checkout
from auto_tests.utils.ui_helpers import register


def test_positive_checkout_process(browser, user_fixture):
    new_user = user_fixture['new_user']
    register(browser, new_user['first_name'], new_user['last_name'], new_user['email'], new_user['password'])
    assert "Register" in browser.title
    login(browser, new_user['email'], new_user['password'])
    assert "Demo Web Shop" in browser.title
    search_product(browser, new_user['product'])
    assert "Search" in browser.title
    add_product_to_cart(browser, new_user['product'])
    assert "Shopping Cart" in browser.title
    checkout(browser, new_user['first_name'], new_user['last_name'], new_user['email'], new_user['country'], new_user['city'], new_user['address'], new_user['postal_code'], new_user['phone'])
    assert "Checkout" in browser.title