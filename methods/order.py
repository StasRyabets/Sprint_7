import requests
import json
from urls import *


def create_order_with_specific_color(first_color=None, second_color=None):
    if first_color is not None and second_color is not None:
        color = [
            first_color,
            second_color
        ]

    elif first_color is not None and second_color is None:
        color = [
            first_color
        ]

    elif first_color is None and second_color is not None:
        color = [
            second_color
        ]

    else:
        color = []

    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": "5",
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": color
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(order_url, json=payload, headers=headers)

    if response.status_code == 201:
        return json.loads(response.content)['track']
    else:
        return response.text


def get_one_order_from_list_with_first_metro_station():
    response = requests.get(order_with_filters_url)
    if response.status_code == 200:
        return json.loads(response.content)['orders']
    else:
        return response.text
