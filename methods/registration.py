import requests
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def register_new_courier_return_credentials_or_response(param=None):
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201 and param == 'credentials':
        login_pass = []
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
        return login_pass

    else:
        return response.text


def register_using_same_credentials():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    return response.text


def register_new_courier_without_required_attribute(attribute=None):
    str = generate_random_string(10)
    first_name = generate_random_string(10)

    if attribute == 'login':
        payload = {
            "password": str,
            "firstName": first_name
        }

    else:
        payload = {
            "login": str,
            "firstName": first_name
        }

    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    return response.text


def register_new_courier_with_specific_data(login=None, password=None, first_name=None):
    login_pass = []
    if login == None:
        login = generate_random_string(10)

    if password == None:
        password = generate_random_string(10)

    if first_name == None:
        first_name = generate_random_string(10)
    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    return response.text
