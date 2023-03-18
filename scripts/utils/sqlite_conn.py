def insert_order(cursor, order, total_price):
    cursor.execute("""
        INSERT INTO `order` (`client_name`, `client_dni`, `client_address`, `client_phone`, `date`, `total_price`, `size_id`)
        VALUES (?, ?, ?, ?, ?, ?, ?)
     """, (order['client_name'], order['client_dni'], order['client_address'],
                 order['client_phone'], order['date'], total_price, order['size_id']['_id']))


def insert_ingredient_detail(cursor, order_id, ingredient_id, ingredient_price):
    cursor.execute("""
        INSERT INTO `ingredient_detail` (`order_id`, `ingredient_id`, `ingredient_price`)
        VALUES (?, ?, ?)
    """, (order_id, ingredient_id, ingredient_price))


def insert_beverage_detail(cursor, order_id, beverage_id, beverage_price):
    cursor.execute("""
        INSERT INTO `beverage_detail` (`order_id`, `beverage_id`, `beverage_price`)
        VALUES (?, ?, ?)
    """, (order_id, beverage_id, beverage_price))


def insert_size(cursor, size):
    cursor.execute('''
        INSERT INTO size (_id, name, price)
        VALUES (?, ?, ?)
    ''', (size))


def insert_ingredient(cursor, ingredient):
    cursor.execute('''
        INSERT INTO ingredient (_id, name, price)
        VALUES (?, ?, ?)
    ''', (ingredient))


def insert_beverage(cursor, beverage):
    cursor.execute('''
        INSERT INTO beverage (_id, name, price, size)
        VALUES (?, ?, ?, ?)
    ''', (beverage))