import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request,render_template, redirect, url_for
from src.api.sql.queries import (CREATE_PRODUCTS_TABLE,
                                 INSERT_PRODUCTS)
from src.api.classes.productClass import Product

load_dotenv()

app = Flask(__name__)
load_dotenv()
url = os.getenv('DATABASE_URL')
connection = psycopg2.connect(url)
product = Product(connection)

# Root URL
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_product')
def get_product():
    return product.getAll()

@app.route('/get_product/<string:id>')
def get_product_by_id(id: str):
    return product.getById(id)

@app.post('/add_product/<string:id>')
def create_product(id: str):
    return product.updateProduct(id)

@app.route('/delete_product/<string:id>')
def delete_product(id: str):
    return product.deleteProduct(id)



if __name__ == '__main__':
    app.run(debug=True)
