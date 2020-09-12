from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Orders:
    def __init__(self, db_conn, order_id, user_id=None, address=None, discount_id=None, product_id=None, quantity=None, status=None, amount=None, creation_date=None, modification_date=None):
        self.tablename = 'orders'
        self.db_conn = db_conn
        self.id = order_id
        self.user_id = user_id
        self.address = address
        self.discount_id = discount_id
        self.product_id = product_id
        self.quantity = quantity
        self.status = status
        self.amount = amount
        self.creation_date = creation_date
        self.modification_date = modification_date
    

    def create_order(self):
        cur = self.db_conn.cursor()
        cur.execute("""INSERT into {} (order_id, user_id, address, discount_id, product_id, quantity, status, amount, creation_date, modification_date) VALUES ({},{},{},{},{},{},{},{},{},{})""".format(self.table_name, self.id, self.user_id, self.address, self.discount_id, self.product_id, self.quantity, self.status, self.amount, self.creation_date, self.modification_date))
        cur.close()
        self.db_conn.commit()

    def get_order(self, id = None):
        if id==None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {}""".format(self.table_name))
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(data[0])
        else:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {} where order_id= {}""".format(self.table_name, self.id))
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid Order")
        cur.close()
         

    def update_order(self, id = None):
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE {} SET order_id = {}, user_id={}, address={}, discount_id={}, product_id={}, quantity={}, status={}, amount={} where order_id={}""".format(self.table_name, self.id, self.user_id, self.address, self.discount_id, self.product_id, self.quantity, self.status, self.amount, self.creation_date, self.modification_date, id))
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid Order")
        cur.close()
        self.db_conn.commit()

    def delete_order(self, id = None):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE {} where order_id={}""".format(self.table_name, self.id))
        cur.close()
        self.db_conn.commit()  
            