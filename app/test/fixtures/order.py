import pytest
from scripts.seed_constants import BEVERAGE_CHOICES, INGREDIENT_CHOICES, SIZE_CHOICES

from scripts.utils.pizza_faker import generate_client_names, generate_random_order

from ..utils.functions import (shuffle_list, get_random_sequence,
                               get_random_string)


def client_data_mock() -> dict:
    return {
        'client_address': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    }



@pytest.fixture
def fake_orders_with_mock_data() -> list:
    clients = generate_client_names(14)
    orders = []
    for _ in range(10):
        order, ingredient_details, beverage_details, total_price = generate_random_order(
            clients, SIZE_CHOICES, INGREDIENT_CHOICES, BEVERAGE_CHOICES)
        order_dict = {**order, 'ingredient_detail': ingredient_details,
                      'beverage_detail': beverage_details, 'total_price': total_price}
        orders.append(order_dict)

    return orders


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def order(create_ingredients, create_beverages, create_size, client_data) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.get('_id')
    return {
        **client_data_mock(),
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }


def create_order(client, order_uri, create_ingredients, create_beverages, create_sizes):
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    sizes = [size.get('_id') for size in create_sizes]
    order = client.post(order_uri, json={
        **client_data_mock(),
        'ingredients': shuffle_list(ingredients)[:5],
        'beverages': shuffle_list(beverages)[:5],
        'size_id': shuffle_list(sizes)[0]
    })
    return order


@pytest.fixture
def create_order_dict(client, order_uri, create_ingredients, create_beverages, create_sizes) -> dict:
    return create_order(client, order_uri, create_ingredients, create_beverages, create_sizes)


@pytest.fixture
def create_orders_list(client, order_uri, create_ingredients, create_beverages, create_sizes) -> list:
    orders = []
    for _ in range(10):
        new_order = create_order(
            client, order_uri, create_ingredients, create_beverages, create_sizes)
        orders.append(new_order)
    return orders
