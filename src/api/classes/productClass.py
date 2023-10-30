from src.api.sql.queries import (SELECT_ALL_PRODUCTS,
                                 CREATE_PRODUCTS_TABLE,
                                 INSERT_PRODUCTS)
from flask import request

class Product:
    def __init__(self, conn):
        self._connection = conn
        self._cursor = conn.cursor()
        
    def getAll(self):
        try:
            self._cursor.execute(SELECT_ALL_PRODUCTS)
            results = self._cursor.fetchall()
            return results
        except Exception as e:
            raise Exception from e
        
    def getById(self, id):
        try:
            query = F"SELECT * FROM products WHERE id = {id}"
            self._cursor.execute(query)
            results = self._cursor.fetchall()
            return results
        except Exception as e:
            raise Exception from e
        
    def createProduct(self):
        try:
            data = request.get_json()
            product_name = data['product_name']
            description = data['description']
            stock_available = data['stock_available']
            image = data['image']
            self._cursor.execute(CREATE_PRODUCTS_TABLE)
            self._cursor.execute(INSERT_PRODUCTS, (product_name, description, stock_available, image,))
            self._connection.commit()
            id_product = self._cursor.fetchone()[0]
            return {"id": id_product, "message": f"Product {product_name} created."}, 201
        except Exception as e:
            raise Exception from e
            
    def updateProduct(self, id):
        try:
            data = request.get_json()
            product_name = data['product_name']
            description = data['description']
            stock_available = data['stock_available']
            image = data['image']
            query = f"""UPDATE products
                    SET product_name = '{product_name}', description = '{description}', stock_available = '{stock_available}', image = '{image}'
                    WHERE id = {id}"""
            self._cursor.execute(query)
            self._connection.commit()
            return {"id": id, "message": f"Product with id {id} updated."}, 201
        except Exception as e:
            print(e)
            raise Exception from e

    def deleteProduct(self, id):
        try:
            query = f"DELETE FROM products WHERE id={id};"
            self._cursor.execute(query)
            self._connection.commit()
            return {"id": id, "message": f"Product with id {id} deleted."}, 201
        except Exception as e:
            print(e)
            raise Exception from e