import sqlite3


# def create_connection(db_name):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_name)
#     except sqlite3.Error as e:
#         print(e)
#     return connection


# def create_table(connection, create_table_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_sql)
#     except sqlite3.Error as e:
#         print(e)

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


# def insert_employee(connection, employee):
#     sql = '''INSERT INTO employees 
#     (full_name, salary, hobby, birth_date, is_married)
#     VALUES (?, ?, ?, ?, ?)'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, employee)
#         connection.commit()
#     except sqlite3.Error as e:
#         print(e)


def insert_employee(db_name, employee):
    sql = '''INSERT INTO employees 
    (full_name, salary, hobby, birth_date, is_married)
    VALUES (?, ?, ?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
            connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_employee(db_name, id):
    sql = '''DELETE FROM employees WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_employee(db_name, employee):
    sql = '''UPDATE employees SET salary = ?, is_married = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
            connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_employees(db_name):
    sql = '''SELECT * FROM employees'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_employees_by_salary(db_name, salary_limit):
    sql = '''SELECT id, full_name, salary FROM employees WHERE salary >= ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (salary_limit,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


db_name = '''group_50.db'''
sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(200) NOT NULL,
    salary FLOAT(10, 2) DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    is_married BOOLEAN DEFAULT FALSE
)
'''

# my_connection = create_connection(db_name)
# if my_connection is not None:
#     print('Connection established')
#     # create_table(my_connection, sql_to_create_employees_table)
#     insert_employee(my_connection, ('Ademi', 2900.7, 'Programming', '2000-01-29', True))
#     my_connection.close()

# create_table(db_name, sql_to_create_employees_table)
# insert_employee(db_name, ('Ademi', 2900.7, 'Programming', '2000-01-29', True))
# insert_employee(db_name, ('Mark Daniels', 1500.0, 'Football', '1999-01-02', False))
# insert_employee(db_name, ('Alex Brilliant', 2300.5, None, '1989-12-31', True))
# insert_employee(db_name, ('Diana Julls', 1800.0, 'Programming', '2005-01-22', True))
# insert_employee(db_name, ('Michael Corse', 1800.0, 'Football', '2001-09-17', True))
# insert_employee(db_name, ('Jack Moris', 2100.2, 'Programming', '2001-07-12', True))
# insert_employee(db_name, ('Viola Manilson', 1750.82, None, '1991-03-01', False))
# insert_employee(db_name, ('Joanna Moris', 1000.0, 'Football', '2004-04-13', False))
# insert_employee(db_name, ('Peter Parker', 2000.0, 'Programming', '2002-11-28', False))
# insert_employee(db_name, ('Paula Parkerson', 800.09, None, '2001-11-28', True))
# insert_employee(db_name, ('George Newel', 1320.0, 'Programming', '1981-01-24', True))
# insert_employee(db_name, ('Miranda Alistoun', 2500.55, 'Football', '1997-12-22', False))
# insert_employee(db_name, ('Valeria Hillton', 2000, 'Football', '1977-10-28', True))
# insert_employee(db_name, ('Jannet Miler', 2100.9, 'Programming', '1997-02-02', True))
# insert_employee(db_name, ('William Tokenson', 1500, None, '1999-12-12', False))
# insert_employee(db_name, ('Shanty Morani', 1200.6, None, '1989-08-13', False))
# insert_employee(db_name, ('Fiona Giordano', 900.12, 'Football', '1977-01-15', True))
# delete_employee(db_name, 2)
# update_employee(db_name, (2300, False, 19))
# select_all_employees(db_name)
select_employees_by_salary(db_name, 2000)