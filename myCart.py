from config.config import get_config
from db.connector.connection import connect_to_db
from db.models.user import User
from db.models.category import Category
from db.models.products import Products
from db.models.discount import Discount
from db.models.orders import Orders
from db.models.userCart import User_cart
from db.models.cartInfo import Cart_info
from datetime import datetime
import uuid

config_path = "/home/diksha/Interview/Work/MyCart-App/config/configuration.json"

if __name__ == "__main__":
    config = get_config(config_path)
    db_conn = connect_to_db(
        config["db"], config["host"], config["user"], config["password"])

    # User Operations
    # CREATE
    user = User(db_conn, first_name="Saavi", last_name='Sirsat',
                email='saavisirsatgmail.com', contact_number=1234567890,
                address='Pune', postal_code='411031', password='hello1234', user_type=1)
    user.create_user()

    user = User(db_conn, first_name="Priya", last_name='Sirsat',
                email='saavisirsatgmail.com', contact_number=1234567890,
                address='Pune', postal_code='411031', password='hello1234', user_type=1)
    user.create_user()

    # GET
    user = User(db_conn)
    user.get_user(2)

    # UPDATE
    user = User(db_conn)
    user.update_user(1, first_name="Gauri", last_name='Darade',
                     email='gaurigmail.com', contact_number=1234567890,
                     address='Pune', postal_code='411031', password='hello1234', user_type=1)

    # Category Operations
    # CREATE
    category = Category(db_conn, cname="Casual", info='Good for everyday',
                        is_deleted=0)
    category.create_category()

    # GET
    category = Category(db_conn)
    cat_info = category.get_category()

    # UPDATE
    category = Category(db_conn)
    category.update_category(
        1, cname="Formal", info='Good for everyday', is_deleted=0)

    # Products Operation
    product = Products(db_conn, product_name="Levis Jeans", category_id=1,
                       info='Comfortable', color='Blue', product_size=30, price=2000)
    product.create_product()

    # GET
    product = Products(db_conn)
    product.get_product()

    # UPDATE
    '''product = Products(db_conn)
    product.update_product(1, product_name='Levis', category_id=1,
                           info='Funky & Comfortable', color='Blue', product_size=30, price=2000)'''

    # Discount Operations
    discount = Discount(db_conn, name="Discount",
                        amount=10000, discount=500, discount_type=True)
    discount.create_discount()

    # GET
    discount = Discount(db_conn)
    disc_info = discount.get_discount()

    # UPDATE
    discount = Discount(db_conn)
    discount.update_discount(1, name="Normal discount",
                             amount=10050, discount=500, discount_type=True)

    # Orders Operations
    # CREATE
    orders = Orders(db_conn, user_id=1, address="Pimpri Chinchwad",
                    discount_id=1, product_id=1, quantity=2, status="Packed", amount=3500)
    orders.create_order()

    orders = Orders(db_conn, user_id=2, address="Pune",
                    discount_id=1, product_id=1, quantity=4, status="Dispatched", amount=5000)
    orders.create_order()

    # GET
    orders = Orders(db_conn)
    order_info = orders.get_order()

    # UPDATE

    orders = Orders(db_conn)
    orders.update_order(1, user_id=2, address="Navi Mumbai",
                        discount_id=1, product_id=1, quantity=4, status="Dispatched", amount=5000)

    # UserCart Operations
    # CREATE
    cart = User_cart(db_conn, order_id=1, saved_for_later=False, quantity=1)
    cart.create_cart()

    # GET
    cart = User_cart(db_conn)
    cart_info = cart.get_cart()

    # UPDATE
    cart = User_cart(db_conn)
    cart.update_cart(1, order_id=1, saved_for_later=False, quantity=5)

    '''# Cart Info Operations
    cart_info = Cart_info(db_conn, cart_id=1, order_id=1, product_id=1)
    cart_info.create_cart()

    cart_info = Cart_info(db_conn)
    cart_info.get_cart_info()


is_logged_in = False
is_app_running = True
while(is_app_running):
    user_name = input("Enter your user name:")
    pwd = input("Enter your password")'''
