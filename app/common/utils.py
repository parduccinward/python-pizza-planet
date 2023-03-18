
def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)


def response_to_dict(response, key):
    data_dict = {}
    for item in response.json:
        data_dict[item[key]] = item
    return data_dict

def _get_status_code(orders, error):
    if orders:
        return 200
    elif error:
        return 400
    else:
        return 404