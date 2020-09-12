from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Products:
    def __init__(self, db_conn, product_id, product_name=None, category_id=None, info=None, color=None,product_size=None, price=None, creation_date=None):
        self.tablename = 'products'
        self.db_conn = db_conn
        self.id = product_id
        self.product_name = product_name
        self.category_id = category_id
        self.info = info
        self.color = color
        self.product_size = product_size
        self.price = price
        self.creation_date = creation_date


    def create_product(self):
        cur = self.db_conn.cursor()
        cur.execute("""INSERT into {} (product_id,product_name, category_id, info, color, product_size, price, creation_date) VALUES ({},{},{},{},{},{},{})""".format(self.table_name ,self.id,self.product_name,self.category_id,self.color, self.product_size, self.price, self.creation_date))
        cur.close()
        self.db_conn.commit()

    def get_product(self, id = None):
        if id==None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {}""".format(self.table_name))
            data = cur.fetchall()
            for product in data:
                    usr = user_data_to_dict(data[0])
        else:
            cur = self.db_conn.cursor()
            cur.execute(("""SELECT * from {} where product_id= {}""".format(self.table_name, self.id))
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid product")
        cur.close()
         

    def update_product(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE {} SET product_id={},product_name={},category_id={}, info={}, color={},product_size={}, price={},creation_date={} where product_id={}""".format(self.table_name, self.id, self.product_name, self.category_id, self.info, self.color, self.product_size, self.price, creation_date, id))
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid product")
        cur.close()
        self.db_conn.commit()

    def delete_product(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE {} where product_id={}""".format(self.table_name, self.id))
        cur.close()
        self.db_conn.commit()  
              