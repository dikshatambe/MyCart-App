from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class Category:
    def __init__(self, db_conn, category_id, cname=None, info=None):
        self.tablename = 'category'
        self.db_conn = db_conn
        self.id = category_id
        self.cname = cname
        self.info = info
     

    def create_category(self):
        cur = self.db_conn.cursor()
        cur.execute('INSERT into self.table_name (category_id,cname,info) VALUES (self.id, self.cname,self.info);')
        cur.close()
        self.db_conn.commit()
     

    def get_category(self, id = None):
        if id==None:
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name')
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(data[0]
        else:
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name where category_id=id;')
            data = cur.fetchall()
            if len(data) >0:
            else:
                print("Invalid category")
        cur.close()
         

    def update_category(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute('UPDATE self.table_name SET category_id=self.category_id,cname=self.cname, info=self.info where categoy_id=id;')
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid category")
        cur.close()
        self.db_conn.commit()

    def delete_category(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute('DELETE self.table_name where category_id=id;')
        cur.close()
        self.db_conn.commit()       

        