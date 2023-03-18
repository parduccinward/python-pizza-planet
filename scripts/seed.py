import sqlite3
from seed_constants import BEVERAGE_CHOICES, INGREDIENT_CHOICES, SIZE_CHOICES
from utils.pizza_faker import generate_client_names, generate_random_order
from utils.sqlite_conn import insert_beverage, insert_beverage_detail, insert_ingredient, insert_ingredient_detail, insert_order, insert_size


conn = sqlite3.connect('pizza.sqlite')
cursor = conn.cursor()

clients = generate_client_names(60)

for orders in range(100):
    order, ingredient_details, beverage_details, total_price = generate_random_order(
        clients, SIZE_CHOICES, INGREDIENT_CHOICES, BEVERAGE_CHOICES)
    insert_order(cursor, order, total_price)
    order_id = cursor.lastrowid

    for ingredient in ingredient_details:
        ingredient_id = ingredient['ingredient']['_id']
        ingredient_price = ingredient['ingredient_price']
        insert_ingredient_detail(
            cursor, order_id, ingredient_id, ingredient_price)

    for beverage in beverage_details:
        beverage_id = beverage['beverage']['_id']
        beverage_price = beverage['beverage_price']
        insert_beverage_detail(cursor, order_id, beverage_id, beverage_price)

for size in SIZE_CHOICES:
    insert_size(cursor, size)

for ingredient in INGREDIENT_CHOICES:
    insert_ingredient(cursor, ingredient)

for beverage in BEVERAGE_CHOICES:
    insert_beverage(cursor, beverage)

conn.commit()
conn.close()
