from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Cart_info:
    def __init__(self, db_conn, cart_id, user_id=None, product_id=None):
        self.tablename = 'cartInfo'
        self.db_conn = db_conn
        self.id = cart_id
        self.user_id = user_id
        self.product_id = product_id
 
    
    def create_cart(self):
        cur = self.db_conn.cursor()
        cur.execute('INSERT into self.table_name (cart_id, user_id, product_id) VALUES (self.id, seld.user_id, self.product_id);')
        cur.close()
        self.db_conn.commit()

    def get_cart_info(self, cart_id = None):
        if id==None:
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name;')
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(data[0])
        else:
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name where cart_id=id')
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid Cart Details")
        cur.close()
         

    def update_cart_info(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute('UPDATE self.table_name SET cart_id = self.id, user_id=self.user_id, product_id=self.product_id where cart_id=id;')
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid Cart")
        cur.close()
        self.db_conn.commit()
       

    def delete_cart_info(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute('DELETE self.table_name where cart_id=id;')
        cur.close()
        self.db_conn.commit()  
        