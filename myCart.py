from config.config import get_config
from db.connector.connection import connect_to_db
from db.models.user import User
from datetime import datetime
import uuid

config_path = "/home/diksha/Interview/Work/MyCart-App/config/configuration.json"

if __name__ == "__main__":
    creation = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #creation = datetime.now()
    config = get_config(config_path)
    db_conn = connect_to_db(config["db"], config["host"], config["user"],config["password"])
    user = User(db_conn, user_id = uuid.uuid4(), first_name="Saavi", last_name="Sirsat",\
         email="saavisirsatgmail.com",contact_number=1234567890,\
             address="Pune",postal_code=411031,password='hello1234',user_type=1, creation_date=creation)
    user.create_user()
