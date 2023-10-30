CREATE_PRODUCTS_TABLE = """CREATE TABLE IF NOT EXISTS products (id SERIAL PRIMARY KEY, product_name VARCHAR(40),
                            description VARCHAR(80), stock_available INTEGER, image VARCHAR(120));"""

INSERT_PRODUCTS = "INSERT INTO products (product_name, description, stock_available, image) VALUES (%s, %s, %s, %s) RETURNING id;"

SELECT_ALL_PRODUCTS = "SELECT * FROM products;"