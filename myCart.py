from config.config import get_config
from db.connector.connection import connect_to_db
from db.models.user import User
from db.models.category import Category
from db.models.products import Products
from datetime import datetime
import uuid

config_path = "/home/diksha/Interview/Work/MyCart-App/config/configuration.json"

if __name__ == "__main__":
    config = get_config(config_path)
    db_conn = connect_to_db(
        config["db"], config["host"], config["user"], config["password"])
    user = User(db_conn, first_name="Saavi", last_name='Sirsat',
                email='saavisirsatgmail.com', contact_number=1234567890,
                address='Pune', postal_code='411031', password='hello1234', user_type=1)
    user.create_user()

    user = User(db_conn)
    info = user.get_user()
    print(info)

    category = Category(db_conn, cname="Casual", info='Good for everyday',
                        is_deleted=0)
    category.create_category()

    category = Category(db_conn)
    cat_info = category.get_category()
    print(cat_info)

    product = Products(db_conn, product_name="Levis Jeans", category_id=1,
                       info='Comfortable', color='Blue', product_size=30, price=2000)
    product.create_product()

    product = Products(db_conn)
    prod_info = product.get_product()
    print(prod_info)

    '''user = User(db_conn, first_name="Saavi", last_name='Shinde',
                email='saavisirsatgmail.com', contact_number=1234567890,
                address='Pune', postal_code='411031', password='hello1234', user_type=1)
    user.update_user()


 
is_logged_in = False
is_app_running = True
while(is_app_running):
    user_name = input("Enter your user name:")
    pwd = input("Enter your password")'''
