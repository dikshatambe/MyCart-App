''''from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Discount:
    def __init__(self, db_conn,id, name=None, amount=None, discount=None, discount_type=None,quantity=None):
        self.tablename = 'discount'
        self.db_conn = db_conn
        self.id = discount_id
        self.name = name
        self.amount = amount
        self.discount = discount
        self.type = discount_type
        self.quantity = quantity
     

    def create_discount(self):
        con = pymysql.connect(hostname, username, password, database)
        cur = con.cursor()
        cur.execute('INSERT into self.table_name ((discount_id,name,amount,discount,discount_type, quantity) values(self.discount_id,self.name,self.amount,self.discount,self.type, self.quantity))')
        cur.close()
        con.commit()
        con.close()

    def get_discount(self, id = None):
        if id==None:
            dis_info =[]
            con = pymysql.connect(hostname, username, password, database)
            cur = con.cursor()
            cur.execute('SELECT * from self.table_name')
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(user)
                    dis_info.append(usr)
            print(dis_info)
        else:
            con = pymysql.connect(hostname, username, password, database)
            cur = con.cursor()
            cur.execute('SELECT * from self.table_name where id=%s')
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
                print(usr)
            else:
                print("Invalid discount")
        cur.close()
        con.commit()
        con.close()
         

    def update_category(self):
        con = pymysql.connect(hostname, username, password, database)
        cur = con.cursor()
        cur.execute('UPDATE self.table_name SET discount_id=self.id,name=self.name, amount=self.amount, discount=self.discount,discount_type=self.type,quantity=self.quantity where id=%s')
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid Discount field")
        cur.close()
        con.commit()
        con.close()

    def delete_category(self):
        con = pymysql.connect(hostname, username, password, database)
        cur = con.cursor()
        cur.execute('DELETE self.table_name where id=%s')
        cur.close()
        con.commit()  
        con.close()      '''