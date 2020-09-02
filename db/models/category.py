'''from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Category:
    def __init__(self, db_conn, id, cname=None, info=None):
        self.tablename = 'category'
        self.db_conn = db_conn
        self.id = category_id
        self.cname = cname
        self.info = info
     

    def create_category(self):
        con = pymysql.connect(hostname, username, password, database)
        cur = con.cursor()
        cur.execute('INSERT into self.table_name ((category_id,cname,info) values(self.id, self.cname,self.info))')
        cur.close()
        con.commit()
        con.close()

    def get_category(self, id = None):
        if id==None:
            cat_info =[]
            con = pymysql.connect(hostname, username, password, database)
            cur = con.cursor()
            cur.execute('SELECT * from self.table_name')
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(user)
                    cat_info.append(usr)
            print(cat_info)
        else:
            con = pymysql.connect(hostname, username, password, database)
            cur = con.cursor()
            cur.execute('SELECT * from self.table_name where id=%s')
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
                print(usr)
            else:
                print("Invalid category")
        cur.close()
        con.commit()
        con.close()
         

    def update_category(self):
        con = pymysql.connect(hostname, username, password, database)
        cur = con.cursor()
        cur.execute('UPDATE self.table_name SET category_id=self.category_id,cname=self.cname, info=self.info where id=%s')
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid category")
        cur.close()
        con.commit()
        con.close()

    def delete_category(self):
        con = pymysql.connect(hostname, username, password, database)
        cur = con.cursor()
        cur.execute('DELETE self.table_name where id=%s')
        cur.close()
        con.commit()  
        con.close()      

        

   '''