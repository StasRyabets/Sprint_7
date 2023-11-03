import pytest
import allure 
from methods.registration import *
from data import Registration

class TestRegistration:
    def test_successful_registration_with_random_data(self):
        assert register_new_courier() == Registration.response_200

    def test_register_using_same_credentials(self):
        assert register_using_same_credentials() == Registration.response_409

    @pytest.mark.parametrize('attribute', ['login', 'password'])
    def test_register_new_courier_without_required_attribute(self, attribute):
        assert register_new_courier_without_required_attribute(attribute) == Registration.response_400

    def test_register_new_courier_with_empty_fields(self):
        assert register_new_courier_with_specific_data('', '', '') == Registration.response_400

    def test_register_new_courier_with_same_login(self):
        login = generate_random_string(7)
        register_new_courier_with_specific_data(login)
        assert register_new_courier_with_specific_data(login) == Registration.response_409
