import json
import pytest

from app.test.utils.functions import get_random_price, get_random_string


def test_create_size_service(create_size):
    size = create_size.json
    pytest.assume(create_size.status.startswith('200'))
    pytest.assume(size["_id"])
    pytest.assume(size["name"])
    pytest.assume(size["price"])


def test_update_size_service(client, create_size, size_uri):
    size_to_update = create_size.json
    updated_size = {**size_to_update,
                    "name": get_random_string(), "price": get_random_price(1, 5)}
    response = client.put(size_uri, json=updated_size)
    pytest.assume(response.status.startswith('200'))
    pytest.assume(json.loads(response.data.decode()) == updated_size)


def test_get_size_by_id_service(client, create_size, size_uri):
    selected_size = create_size.json
    response = client.get(f'{size_uri}id/{selected_size["_id"]}')
    pytest.assume(response.status.startswith('200'))
    pytest.assume(json.loads(response.data.decode()) == selected_size)


def test_get_sizes_service(client, create_sizes, size_uri):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith('200'))

    response_size = {size["_id"]: size for size in response.json}
    for size in create_sizes:
        pytest.assume(size["_id"] in response_size)
