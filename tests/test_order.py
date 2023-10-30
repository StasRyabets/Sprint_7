import pytest
import allure 
from methods.order import *


@pytest.mark.parametrize(
    'first_color, second_color',
    [
        ['BLACK', 'GREY'],
        ['BLACK', None],
        [None, 'GREY'],
        [None, None]
    ]
)
def test_create_order_with_specific_color(first_color, second_color):
    assert isinstance(create_order_with_specific_color(first_color, second_color), int) 

def test_get_order_with_filters():
    orders = get_one_order_from_list_with_first_metro_station()
    for order in orders:
        assert isinstance(order['id'], int)