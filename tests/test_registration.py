import pytest
import allure 
from methods.registration import *

def test_successful_registration_with_random_data():
    assert register_new_courier_return_credentials_or_response() == '{"ok":true}'

def test_register_using_same_credentials():
    assert register_using_same_credentials() == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

@pytest.mark.parametrize('attribute', ['login', 'password'])
def test_register_new_courier_without_required_attribute(attribute):
    assert register_new_courier_without_required_attribute(attribute) == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

def test_register_new_courier_with_empty_fields():
    assert register_new_courier_with_specific_data('', '', '') == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

def test_register_new_courier_with_same_login():
    login = generate_random_string(7)
    register_new_courier_with_specific_data(login)
    assert register_new_courier_with_specific_data(login) == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'