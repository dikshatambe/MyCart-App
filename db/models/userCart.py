'''from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class User_cart:
    def __init__(self, db_conn, id, user_id=None, product_id=None, saved_for_later=None, quantity=None):
        self.tablename = 'userCart'
        self.db_conn = db_conn
        self.id = cart_id
        self.user_id = user_id
        self.product_id = product_id
        self.saved_for_later=saved_for_later
        self.quantity = quantity
    

    def create_cart(self):
        cur = self.db_conn.cursor()
        cur.execute('INSERT into self.table_name ((cart_id, user_id, product_id, saved_for_later, quantity) values(self.id, seld.user_id, self.product_id, self.saved_for_later, self.quantity))')
        cur.close()
        self.db_conn.commit()

    def get_cart(self, id = None):
        if id==None:
            cart_info =[]
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name')
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(user)
                    cart_info.append(usr)
        else:
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name where id=%s')
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid Cart Details")
        cur.close()
         

    def update_cart(self):
        cur = self.db_conn.cursor()
        cur.execute('UPDATE order_id = self.id, user_id=self.user_id, product_id=self.product_id, saved_for_later=self.saved_for_later, quantity=self.quantity where id=%s')
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid Cart")
        cur.close()
        self.db_conn.commit()

    def delete_cart(self):
        cur = self.db_conn.cursor()
        cur.execute('DELETE self.table_name where id=%s')
        cur.close()
        self.db_conn.commit()  
    '''