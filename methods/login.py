import requests
import json


def login_user(login='', password=''):

    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    
    if response.status_code == 200:
        return json.loads(response._content)['id']
    else:
        return response.text
    
# login = 'stanislavchik'
# print(login_user(login[:-0], '12345'))

