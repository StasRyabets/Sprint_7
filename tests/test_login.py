import pytest
import allure
from methods.registration import *
from methods.login import *
from data import Login


class TestLogin:
    def test_successful_login(self):
        login = generate_random_string(7)
        password = generate_random_string(6)
        register_new_courier_with_specific_data(login, password)
        assert isinstance(login_user(login, password), int)

    @pytest.mark.parametrize(
        'login, password',
        [
            [generate_random_string(7), ''],
            ['', generate_random_string(7)]
        ]
    )
    def test_login_without_required_attribute(self, login, password):
        assert login_user(
            login, password) == Login.response_400

    @pytest.mark.parametrize(
        'chars_remove_from_login, chars_remove_from_password',
        [
            [0, 1],
            [1, 0],
        ]
    )
    def test_login_with_typo(self, chars_remove_from_login, chars_remove_from_password):
        login = generate_random_string(8)
        password = generate_random_string(9)
        register_new_courier_with_specific_data(login, password)
        if chars_remove_from_login == 0:
            login_with_typo = login_user(
                login, password[:-chars_remove_from_password])
        elif chars_remove_from_password == 0:
            login_with_typo = login_user(
                login[:-chars_remove_from_login], password)
        assert login_with_typo == Login.response_404
