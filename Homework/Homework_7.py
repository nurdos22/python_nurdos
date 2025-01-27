import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection):
    sql = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT  ,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    );
    '''
    cursor = connection.cursor()
    cursor.execute(sql)
    print("Таблица products создана")


def add_products(connection):
    sql = '''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?);
    '''
    products = [
        ("Товар 1", 50.5, 10),
        ("Товар 2", 30.0, 5),
        ("Товар 3", 15.75, 20),
        ("Товар 4", 120.99, 8),
        ("Товар 5", 5.0, 50),
        ("Товар 6", 99.99, 15),
        ("Товар 7", 10.0, 30),
        ("Товар 8", 25.0, 12),
        ("Товар 9", 60.0, 6),
        ("Товар 10", 7.5, 100),
        ("Товар 11", 200.0, 2),
        ("Товар 12", 15.0, 7),
        ("Товар 13", 300.0, 1),
        ("Товар 14", 45.0, 18),
        ("Товар 15", 80.0, 3),
    ]
    cursor = connection.cursor()
    cursor.executemany(sql, products)
    connection.commit()
    print("15 товаров добавлены")

def update_quantity(connection, product_id, new_quantity):
    sql = '''
    UPDATE products
    SET quantity = ?
    WHERE id = ?;
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (new_quantity, product_id))
    connection.commit()
    print(f"Количество товара с ID {product_id} изменено на {new_quantity}")


def update_price(connection, product_id, new_price):
    sql = '''
    UPDATE products
    SET price = ?
    WHERE id = ?;
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (new_price, product_id))
    connection.commit()
    print(f"Цена товара с ID {product_id} изменена на {new_price}")


def delete_product(connection, product_id):
    sql = '''
    DELETE FROM products
    WHERE id = ?;
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (product_id,))
    connection.commit()
    print(f"Товар с ID {product_id} удалён")


def select_all_products(connection):
    sql = '''
    SELECT * FROM products;
    '''
    cursor = connection.cursor()
    cursor.execute(sql)
    products = cursor.fetchall()
    for product in products:
        print(product)


def select_products_by_limits(connection, price_limit, quantity_limit):
    sql = '''
    SELECT * FROM products
    WHERE price < ? AND quantity > ?;
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (price_limit, quantity_limit))
    products = cursor.fetchall()
    for product in products:
        print(product)


def search_products_by_name(connection, search_term):
    sql = '''
    SELECT * FROM products
    WHERE product_title LIKE ?;
    '''
    cursor = connection.cursor()
    cursor.execute(sql, (f"%{search_term}%",))
    products = cursor.fetchall()
    for product in products:
        print(product)


if __name__ == "__main__":
    db_name = "hw.db"
    connection = create_connection(db_name)

    create_table(connection)
    add_products(connection)

    print("\nВсе товары:")
    select_all_products(connection)

    print("\nИзменение количества товара:")
    update_quantity(connection, 1, 25)
    select_all_products(connection)

    print("\nИзменение цены товара:")
    update_price(connection, 2, 99.99)
    select_all_products(connection)

    print("\nУдаление товара:")
    delete_product(connection, 3)
    select_all_products(connection)

    print("\nТовары дешевле 100 и количеством больше 5:")
    select_products_by_limits(connection, 100, 5)

    print("\nПоиск товаров с названием 'Товар':")
    search_products_by_name(connection, "Товар")

    connection.close()