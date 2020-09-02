'''from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Cart_info:
    def __init__(self, db_conn, id, user_id=None, product_id=None):
        self.tablename = 'cartInfo'
        self.db_conn = db_conn
        self.id = cart_id
        self.user_id = user_id
        self.product_id = product_id
 
    
    def create_cart(self):
        con = pymysql.connect(hostname, username, password, database)
        cur = con.cursor()
        cur.execute('INSERT into self.table_name ((cart_id, user_id, product_id) values(self.id, seld.user_id, self.product_id))')
        cur.close()
        con.commit()
        con.close()

    def get_cart_info(self, id = None):
        if id==None:
            cart_info =[]
            con = pymysql.connect(hostname, username, password, database)
            cur = con.cursor()
            cur.execute('SELECT * from self.table_name')
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(user)
                    cart_info.append(usr)
            print(cart_info)
        else:
            con = pymysql.connect(hostname, username, password, database)
            cur = con.cursor()
            cur.execute('SELECT * from self.table_name where id=%s')
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
                print(usr)
            else:
                print("Invalid Cart Details")
        cur.close()
        con.commit()
        con.close()
         

    def update_cart_info(self):
        con = pymysql.connect(hostname, username, password, database)
        cur = con.cursor()
        cur.execute('UPDATE order_id = self.id, user_id=self.user_id, product_id=self.product_id where id=%s')
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid Cart")
        cur.close()
        con.commit()
        con.close()

    def delete_cart_info(self):
        con = pymysql.connect(hostname, username, password, database)
        cur = con.cursor()
        cur.execute('DELETE self.table_name where id=%s')
        cur.close()
        con.commit()  
        con.close()      '''