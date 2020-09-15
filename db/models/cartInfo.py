from utils.dict import user_data_to_dict, unicode_to_str, fill_all_field_in_arg
from utils.dict import raw_data_to_cartinfo_model


class Cart_info:
    def __init__(self, cart_id, db_conn=None, user_id=None, product_id=None, creation_date=None):
        self.table_name = 'cartInfo'
        self.db_conn = db_conn
        self.id = cart_id
        self.user_id = user_id
        self.product_id = product_id
        self.creation_date = creation_date

    def create_cart(self):
        cur = self.db_conn.cursor()
        cur.execute("""INSERT into {} (cart_id, user_id, product_id) VALUES ({},{},{})""".format(
            self.table_name, self.id, self.user_id, self.product_id))
        cur.close()
        self.db_conn.commit()

    def get_cart_info(self, cart_id=None):
        if cart_id == None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {} """.format(self.table_name))
            data = cur.fetchall()
            print(data)
            cart_list = []
            for cart in data:
                usr = User_cart()
                usr = raw_data_to_cartinfo_model(cart, usr)
                cart_list.append(usr)
            return cart_list
        else:
            cur = self.db_conn.cursor()
            cur.execute(
                """SELECT * from {} where cart_id= {} """.format(self.table_name, self.id))
            data = cur.fetchall()
            if len(data) > 0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid Cart Details")
        cur.close()

    def update_cart_info(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE {} SET cart_id = {}, user_id={}, product_id={}, creation_date={} where cart_id={} """.format(
            self.table_name, self.id, self.user_id, self.product_id, self.creation_date, id))
        data = cur.fetchall()
        if len(data) > 0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid Cart")
        cur.close()
        self.db_conn.commit()

    def delete_cart_info(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE {} where cart_id={} """.format(
            self.table_name, self.id))
        cur.close()
        self.db_conn.commit()
