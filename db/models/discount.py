from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Discount:
    def __init__(self, db_conn, discount_id, name=None, amount=None, discount=None, discount_type=None,quantity=None, creation_date=None):
        self.tablename = 'discount'
        self.db_conn = db_conn
        self.id = discount_id
        self.name = name
        self.amount = amount
        self.discount = discount
        self.type = discount_type
        self.quantity = quantity
        self.creation_date = creation_date
     

    def create_discount(self):
        cur = self.db_conn.cursor()
        cur.execute("""INSERT into {} (discount_id,name,amount,discount,discount_type, quantity, creation_date) VALUES ({},{},{},{},{},{},{})""".format(self.table_name,self.discount_id,self.name,self.amount,self.discount,self.type, self.quantity, self.creation_date))
        cur.close()
        self.db_conn.commit()

    def get_discount(self, id = None):
        if id==None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {}""".format(self.table_name))
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(data[0])
        else:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {} where discount_id= {}""".format(self.table_name, self.id))
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid discount")
        cur.close()

    def update_category(self, id = None):
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE {} SET discount_id={},name={}, amount={}, discount={},discount_type={},quantity={} where product_id={}""".format(self.table_name, self.table_name,self.discount_id,self.name,self.amount,self.discount,self.type, self.quantity, self.creation_date, id))
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid Discount field")
        cur.close()
        self.db_conn.commit()

    def delete_category(self, id = None):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE {} where discount_id={}""".format(self.table_name, self.id))
        cur.close()
        self.db_conn.commit()  
    