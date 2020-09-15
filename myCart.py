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
    user = User(db_conn, first_name="Saavi", last_name='Sirsat',
                email='saavisirsatgmail.com', contact_number=1234567890,
                address='Pune', postal_code='411031', password='hello1234', user_type=0)
    user.create_user()

    user = User(db_conn)
    info = user.get_user()

    # Category Operations
    category = Category(db_conn, cname="Casual", info='Good for everyday',
                        is_deleted=0)
    if user.user_type == 1:
        category.create_category()
    else:
        print('Not Authorized to create new category')

    category = Category(db_conn)
    cat_info = category.get_category()

    # Products Operation
    product = Products(db_conn, product_name="Levis Jeans", category_id=1,
                       info='Comfortable', color='Blue', product_size=30, price=2000)
    if user.user_type == 1:
        product.create_product()
    else:
        print('Not Authorized to create new products')

    product = Products(db_conn)
    prod_info = product.get_product()

    # Discount Operations
    discount = Discount(db_conn, name="Discount",
                        amount=10000, discount=500, discount_type=True)
    discount.create_discount()

    discount = Discount(db_conn)
    disc_info = discount.get_discount()

    # Orders Operations
    orders = Orders(db_conn, user_id=1, address="Pimpri Chinchwad",
                    discount_id=1, product_id=1, quantity=2, status="Packed", amount=3500)
    orders.create_order()

    orders = Orders(db_conn)
    order_info = orders.get_order()

    # UserCart Operations
    cart = User_cart(db_conn, order_id=1, saved_for_later=False, quantity=1)
    cart.create_cart()

    cart = User_cart(db_conn)
    cart_info = cart.get_cart()

    # Cart Info Operations
    '''cart = Cart_info(db_conn, cart_id=1, order_id=1, product_id=1)
    cart.create_cart()

    cart = Cart_info(db_conn)
    if user.user_type == 1:
        cart_info = cart.get_cart_info()
    else:
        print("Not Authorized")
    #print(cart_info)

    user = User(db_conn, first_name="Saavi", last_name='Shinde',
                email='saavisirsatgmail.com', contact_number=1234567890,
                address='Pune', postal_code='411031', password='hello1234', user_type=1)
    user.update_user()


 
is_logged_in = False
is_app_running = True
while(is_app_running):
    user_name = input("Enter your user name:")
    pwd = input("Enter your password")'''
