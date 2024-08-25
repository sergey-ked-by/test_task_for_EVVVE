from auto_tests.utils.ui_helpers import login, search_product
from auto_tests.utils.ui_helpers import register


def test_positive_navigation_and_search(browser, user_fixture):
    new_user = user_fixture['new_user']
    register(browser, new_user['first_name'], new_user['last_name'], new_user['email'], new_user['password'])
    assert "Register" in browser.title
    login(browser, new_user['email'], new_user['password'])
    assert "Demo Web Shop" in browser.title
    search_product(browser, new_user['product'])
    assert "Search" in browser.title
