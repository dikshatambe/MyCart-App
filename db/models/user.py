from utils.dict import user_data_to_dict, unicode_to_str, fill_all_field_in_arg
from utils.dict import raw_data_to_user_model


class User:
    def __init__(self, db_conn=None, user_id=None, first_name=None, last_name=None, email=None, contact_number=None, address=None, postal_code=None, password=None, user_type=None, creation_date=None):
        self.table_name = 'users'
        self.db_conn = db_conn
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact_number = contact_number
        self.address = address
        self.postal_code = postal_code
        self.password = password
        self.user_type = user_type
        self.creation_date = creation_date

    def create_user(self):
        cur = self.db_conn.cursor()
        query = """INSERT INTO {} (first_name,last_name,email,contact_number, address, postal_code, password, user_type) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{})""".format(
            self.table_name, self.first_name, self.last_name, self.email, self.contact_number, self.address, self.postal_code, self.password, self.user_type)
        cur.execute(query)
        cur.close()
        self.db_conn.commit()

    def get_user(self, user_id=None):
        if user_id == None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {}""".format(self.table_name))
            data = cur.fetchall()
            print(data)
            user_list = []
            for user in data:
                usr = User()
                usr = raw_data_to_user_model(user, usr)
                user_list.append(usr)
            return user_list
        else:
            cur = self.db_conn.cursor()
            cur.execute(
                """SELECT * from {} where user_id= {}""".format(self.table_name, self.id))
            data = cur.fetchall()
            if len(data) > 0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid user")
        cur.close()

    def update_user(self, user_id=None):
        cur = self.db_conn.cursor()
        #cur.execute("""UPDATE {} SET user_id={}, first_name={},last_name={}, email={}, contact_number={}, address={}, postal_code={}, password={}, user_type={}, creation_date={} where user_id={}""".format(self.table_name, self.id, self.first_name, self.last_name, self.email, self.contact_number, self.address, self.postal_code, self.password, self.user_type, self.creation_date, self.id))
        cur.execute("""UPDATE {} SET first_name=\"{}\",last_name=\"{}\", email=\"{}\", contact_number=\"{}\", address=\"{}\", postal_code=\"{}\", password=\"{}\", user_type={} where user_id={}""".format(
            self.table_name, self.first_name, self.last_name, self.email, self.contact_number, self.address, self.postal_code, self.password, self.user_type, self.id))
        data = cur.fetchall()
        if len(data) > 0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid user")
        cur.close()
        self.db_conn.commit()

    def delete_user(self, user_id=None):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE FROM {} where user_id={}""".format(
            self.table_name, self.id))
        cur.close()
        self.db_conn.commit()
