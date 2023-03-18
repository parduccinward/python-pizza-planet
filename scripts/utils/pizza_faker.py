import random
from faker import Faker
import datetime

fake = Faker()


def generate_client_names(num_clients):
    clients = [fake.name() for _ in range(num_clients)]
    return clients


def generate_random_order(clients, sizes, ingredients, beverages):

    start_date = datetime.datetime(2022, 1, 1, 0, 0, 0)
    end_date = datetime.datetime.now()

    order = {
        'client_name': clients[random.randint(0, len(clients)-1)],
        'client_dni': fake.random_number(digits=10),
        'client_address': fake.address(),
        'client_phone': fake.phone_number(),
        'date': fake.date_time_between(start_date=start_date, end_date=end_date),
    }

    size_id = random.randint(1, len(sizes))
    price = sizes[size_id-1][2]

    ingredient_details = generate_ingredient_details(ingredients)
    beverage_details = generate_beverage_details(beverages)

    total_price = calculate_total_price(
        price, ingredient_details, beverage_details)

    order['size_id'] = {
        "_id":size_id,
        "name":sizes[size_id-1][1],
        "price":price
    }

    return order, ingredient_details, beverage_details, total_price


def generate_ingredient_details(ingredients):
    ingredient_details = []
    num_ingredient_details = random.randint(2, 8)
    for ingredient in range(num_ingredient_details):
        ingredient_id, ingredient_name, ingredient_price = random.choice(
            ingredients)
        ingredient_details.append({
            "ingredient": {
                "_id": ingredient_id,
                "name": ingredient_name,
                "price": float(ingredient_price),
            },
            "ingredient_price": float(ingredient_price)
        })
    return ingredient_details


def generate_beverage_details(beverages):
    beverage_details = []
    num_beverage_details = random.randint(0, 7)
    for i in range(num_beverage_details):
        beverage_id, beverage_name, beverage_price, beverage_size = random.choice(
            beverages)
        beverage_details.append({
            "beverage": {
                "_id": beverage_id,
                "name": beverage_name,
                "price": float(beverage_price),
                "size": beverage_size
            },
            "beverage_price": float(beverage_price)
        })
    return beverage_details


def calculate_total_price(price, ingredient_details, beverage_details):
    total_price: float = price
    for ingredient in ingredient_details:
        total_price += float(ingredient["ingredient_price"])
    for beverage in beverage_details:
        total_price += float(beverage["beverage_price"])
    return total_price
