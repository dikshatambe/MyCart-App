from utils.dict import user_data_to_dict, unicode_to_str, fill_all_field_in_arg
from utils.dict import raw_data_to_cart_model


class User_cart:
    def __init__(self, db_conn=None, user_cart_id=None, order_id=None, saved_for_later=None, quantity=None, creation_date=None):
        self.table_name = 'userCart'
        self.db_conn = db_conn
        self.id = user_cart_id
        self.order_id = order_id
        self.saved_for_later = saved_for_later
        self.quantity = quantity
        self.creation_date = creation_date

    def create_cart(self):
        cur = self.db_conn.cursor()
        cur.execute("""INSERT into {} (order_id, saved_for_later, quantity) VALUES ({}, {}, {})""".format(
            self.table_name, self.order_id, self.saved_for_later, self.quantity))
        cur.close()
        self.db_conn.commit()

    def get_cart(self, id=None):
        if id == None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {}""".format(self.table_name))
            data = cur.fetchall()
            print(data)
            cart_list = []
            for cart in data:
                usr = User_cart()
                usr = raw_data_to_cart_model(cart, usr)
                cart_list.append(usr)
            return cart_list
        else:
            cur = self.db_conn.cursor()
            cur.execute(
                """SELECT * from {} where user_cart_id={}""".format(self.table_name, id))
            data = cur.fetchall()
            if len(data) > 0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid Cart Details")
        cur.close()

    def update_cart(self, user_cart_id, order_id=None, saved_for_later=None, quantity=None):
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE {} SET order_id={}, saved_for_later={}, quantity={} where user_cart_id={}""".format(
            self.table_name, order_id, saved_for_later, quantity, user_cart_id))
        data = cur.fetchall()
        if len(data) <= 0:
            print("Invalid Cart")
        else:
            print("User cart updated successfully!")
        cur.close()
        self.db_conn.commit()

    def delete_cart(self, user_cart_id):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE {} where user_cart_id={}""".format(
            self.table_name, user_cart_id))
        cur.close()
        self.db_conn.commit()
