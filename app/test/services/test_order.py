import pytest

from app.test.utils.functions import get_random_string


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


@pytest.mark.skip(reason="test not implemented yet")
def test_get_order_by_id_service():
    pytest.assume(False)


@pytest.mark.skip(reason="test not implemented yet")
def test_get_orders_service():
    pytest.assume(False)
