from auto_tests.utils.ui_helpers import register


def test_positive_registration(browser, user_fixture):
    new_user = user_fixture['new_user']
    register(browser, new_user['first_name'], new_user['last_name'], new_user['email'], new_user['password'])
    assert "Demo Web Shop. Register" in browser.title