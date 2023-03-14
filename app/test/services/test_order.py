import json
import pytest


def test_create_order_service(create_order_dict):
    order = create_order_dict.json
    pytest.assume(create_order_dict.status.startswith('200'))
    pytest.assume(order['_id'])
    pytest.assume(order['client_address'])
    pytest.assume(order['client_dni'])
    pytest.assume(order['client_name'])
    pytest.assume(order['client_phone'])
    pytest.assume(order['date'])
    pytest.assume(order['detail'])
    pytest.assume(order['size'])


def test_get_order_by_id_service(client, create_order_dict, order_uri):
    current_order = create_order_dict.json
    response = client.get(f'{order_uri}id/{current_order["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_order = response.json
    for param, value in current_order.items():
        pytest.assume(returned_order[param] == value)


def test_get_orders_service(client, create_orders_list, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    response_order = {order["_id"]: order for order in response.json}
    for order in create_orders_list:
        formatted_order = json.loads(order.data.decode())
        pytest.assume(formatted_order["_id"] in response_order)
