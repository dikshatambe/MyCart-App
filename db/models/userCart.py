from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class User_cart:
    def __init__(self, db_conn, user_cart_id, order_id=None, saved_for_later=None, quantity=None, creation_date=None):
        self.tablename = 'userCart'
        self.db_conn = db_conn
        self.id = user_cart_id
        self.order_id = user_id
        self.saved_for_later=saved_for_later
        self.quantity = quantity
        self.creation_date = creation_date

    

    def create_cart(self):
        cur = self.db_conn.cursor()
        cur.execute("""INSERT into {} (user_cart_id, order_id, saved_for_later, quantity, creation_date) VALUES ({}, {}, {}, {}, {})""".format(self.table_name,self.id, seld.order_id, self.saved_for_later, self.quantity, self.creation_date))
        cur.close()
        self.db_conn.commit()

    def get_cart(self, id = None):
        if id==None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {}""".format(self.table_name))
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(data[0])
        else:
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from {} where user_cart_id={}""".format(self.table_name, id))
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid Cart Details")
        cur.close()
         

    def update_cart(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE {} SET user_cart_id = {}, order_id={}, saved_for_later={}, quantity={}, creation_date={} where user_cart_id={}""".format(self.table_name, self.id, self.order_id, self.saved_for_later, self.quantity, self.creation_date ,id))
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid Cart")
        cur.close()
        self.db_conn.commit()

    def delete_cart(self):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE {} where user_cart_id={}""".format(self.table_name, id))
        cur.close()
        self.db_conn.commit()  
