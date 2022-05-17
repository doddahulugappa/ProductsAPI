from settings import app
from flask_sqlalchemy import SQLAlchemy


# Initializing database
db = SQLAlchemy(app)


# the class Product will inherit the db.Model of SQLAlchemy
class Product(db.Model):
    __tablename__ = 'products'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(25), nullable=False)

    def json(self):
        """
        This method we are defining will convert our output to json
        """
        return {'id': self.id, 'name': self.name,
                'price': self.price, 'currency': self.currency}


    @staticmethod
    def add_product(_name, _price, _currency):
        """
        :param _name:
        :param _price:
        :param _currency:
        :return:
        function to add product to database using _name, _price, _currency
        as parameters
        """
        # creating an instance of our Product constructor
        new_product = Product(name=_name, price=_price, currency=_currency)
        db.session.add(new_product)  # add new product to database session
        db.session.commit()  # commit changes to session

    @staticmethod
    def get_all_products():
        """
        function to get all products from database
        """
        return [Product.json(product) for product in Product.query.all()]

    @staticmethod
    def get_product(_id):
        """
        function to get product using the id of the product as parameter
        """
        return [Product.json(Product.query.filter_by(id=_id).first())]
        # Product.json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since id is unique we will only get one result
        # the .first() method will get that first value returned

    @staticmethod
    def update_product(_id, _name, _price, _currency):
        """
        function to update the details of a product using the id, name,
        price and currency as parameters
        """
        product_to_update = Product.query.filter_by(id=_id).first()
        product_to_update.name = _name
        product_to_update.price = _price
        product_to_update.currency = _currency
        db.session.commit()

    @staticmethod
    def delete_product(_id):
        """
        function to delete a product from database using
        the id of the product as a parameter
        """
        Product.query.filter_by(id=_id).delete()
        # filter product by id and delete
        db.session.commit() # committing the new change to our database


if __name__ == "__main__":
    db.create_all()