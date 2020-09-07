'''from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Products:
    def __init__(self, db_conn, id, product_name=None, category_id=None, info=None, color=None,product_size=None, price=None):
        self.tablename = 'products'
        self.db_conn = db_conn
        self.id = product_id
        self.product_name = product_name
        self.category_id = category_id
        self.info = info
        self.color = color
        self.product_size = product_size
        self.price = price


    def create_product(self):
        cur = self.db_conn.cursor()
        cur.execute('INSERT into users ((product_id,product_name, category_id, info, color, product_size, price) values(self.id,self.product_name,self.category_id,self.color, self.product_size, self.price))')
        cur.close()
        self.db_conn.commit()

    def get_product(self, id = None):
        if id==None:
            product_info =[]
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name')
            data = cur.fetchall()
            for product in data:
                    usr = user_data_to_dict(product)
                    product_info.append(usr)
        else:
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name where id=%s')
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid product")
        cur.close()
         

    def update_product(self):
        cur = self.db_conn.cursor()
        cur.execute('UPDATE self.table_name SET product_id=self.id,product_name=self.product_name,category_id=self.category_id, info=self.info, color=self.color,product_size=self.product_size where id=%s')
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid product")
        cur.close()
        self.db_conn.commit()

    def delete_product(self):
        cur = self.db_conn.cursor()
        cur.execute('DELETE self.table_name where id=%s')
        cur.close()
        self.db_conn.commit()  
              

        

   '''