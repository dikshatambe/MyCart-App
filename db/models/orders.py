from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Orders:
    def __init__(self, db_conn, order_id, fuser_id=None, address=None, discount_id=None, product_id=None, quantity=None, status=None, amount=None):
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
    

    def create_order(self):
        cur = self.db_conn.cursor()
        cur.execute('INSERT into self.table_name (order_id, user_id, address, discount_id, product_id, quantity, status, amount) VALUES (self.id, self.user_id, self.address, self.discount_id, self.product_id, self.quantity, self.status, self.amount);')
        cur.close()
        self.db_conn.commit()

    def get_order(self, id = None):
        if id==None:
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name;')
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(data[0])
        else:
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name where order_id=id;')
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid Order")
        cur.close()
         

    def update_order(self, id = None):
        cur = self.db_conn.cursor()
        cur.execute('UPDATE self.table_name SET order_id = self.id, user_id=self.user_id, address=self.address, discount_id=self.discount_id, product_id=self.product_id, quantity=self.quantity, status=self.status, amount=self.amount where order_id=id;')
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid Order")
        cur.close()
        self.db_conn.commit()

    def delete_order(self, id = None):
        cur = self.db_conn.cursor()
        cur.execute('DELETE self.table_name where order_id=id;')
        cur.close()
        self.db_conn.commit()  
            