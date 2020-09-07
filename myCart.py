from config.config import get_config
from db.connector.connection import connect_to_db
from db.models.user import User
config_path = "/home/diksha/Interview/Work/MyCart-App/config/configuration.json"

if __name__ == "__main__":
    config = get_config(config_path)
    db_conn = connect_to_db(config["db"], config["host"], config["user"],config["password"])
    user = User(db_conn, id = 1, first_name="Saavi", last_name="Sirsat",\
         email="saavi@sirsat.com",contact_number=1234567890,\
             address="Pune",postal_code=831002,password='hello@hello',user_type=1)
    user.create_user()
