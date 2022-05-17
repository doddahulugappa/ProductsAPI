# importing libraries
from flask import jsonify, Response, request
from products import Product
from settings import app


# route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Function to get all the products from the database"""
    return jsonify({'Products': Product.get_all_products()})


# route to add new product
@app.route('/products', methods=['POST'])
def add_product():
    """Function to add new product to database"""
    request_data = request.get_json()  # getting data from client
    Product.add_product(request_data["name"], request_data["price"], request_data["currency"])
    response = Response("Product added", 201, mimetype='application/json')
    return response


# route to get product by id
@app.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    return_value = Product.get_product(id)
    return jsonify(return_value)


# route to update product with PUT method
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    """Function to edit product in database using product id"""
    request_data = request.get_json()
    Product.update_product(id, request_data['name'], request_data['price'],  request_data['currency'])
    response = Response("Product Updated", status=200, mimetype='application/json')
    return response


# route to delete product using the DELETE method
@app.route('/products/<int:id>', methods=['DELETE'])
def remove_product(id):
    """Function to delete product from database"""
    Product.delete_product(id)
    response = Response("Product Deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=8000, debug=False, host='0.0.0.0')
