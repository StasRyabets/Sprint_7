import pytest
import allure
from methods.registration import *
from methods.login import *


def test_successful_login():
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
def test_login_without_required_attribute(login, password):
    assert login_user(
        login, password) == '{"code":400,"message":"Недостаточно данных для входа"}'


@pytest.mark.parametrize(
    'chars_remove_from_login, chars_remove_from_password',
    [
        [0, 1],
        [1, 0],
    ]
)
def test_login_with_typo(chars_remove_from_login, chars_remove_from_password):
    login = generate_random_string(8)
    password = generate_random_string(9)
    register_new_courier_with_specific_data(login, password)
    if chars_remove_from_login == 0:
        assert login_user(login, password[:-chars_remove_from_password]
                          ) == '{"code":404,"message":"Учетная запись не найдена"}'
    elif chars_remove_from_password == 0:
        assert login_user(login[:-chars_remove_from_login],
                          password) == '{"code":404,"message":"Учетная запись не найдена"}'
