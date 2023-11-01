import pytest
import allure 
from methods.registration import *
from data import Registration

def test_successful_registration_with_random_data():
    assert register_new_courier_return_credentials_or_response() == Registration.response_200

def test_register_using_same_credentials():
    assert register_using_same_credentials() == Registration.response_409

@pytest.mark.parametrize('attribute', ['login', 'password'])
def test_register_new_courier_without_required_attribute(attribute):
    assert register_new_courier_without_required_attribute(attribute) == Registration.response_400

def test_register_new_courier_with_empty_fields():
    assert register_new_courier_with_specific_data('', '', '') == Registration.response_400

def test_register_new_courier_with_same_login():
    login = generate_random_string(7)
    register_new_courier_with_specific_data(login)
    assert register_new_courier_with_specific_data(login) == Registration.response_409
