from utils.dict import user_data_to_dict, unicode_to_str,fill_all_field_in_arg

class User:
    def __init__(self, db_conn, id, first_name=None, last_name=None, email=None, contact_number=None,address=None, postal_code=None, password=None, user_type=None, creation_date=None):
        self.table_name = 'users'
        self.db_conn = db_conn
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact_number = contact_number
        self.address = address
        self.postal_code = postal_code
        self.password = password
        self.user_type = user_type
        #self.creation_date = creation_date


    def create_user(self):
        #con = pymysql.connect(hostname, username, password, database)
        cur = self.db_conn.cursor()
        cur.execute('INSERT into self.table_name(id, first_name,last_name,email,contact_number, address, postal_code, password, user_type) VALUES(self.id, self.first_name,self.last_name,self.email,self.contact_number, self.address, self.postal_code, self.password, self.user_type)')
        cur.close()
        self.db_conn.commit()

    def get_user(self, id = None):
        if id==None:
            user_info =[]
            #con = pymysql.connect(hostname, username, password, database)
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name')
            data = cur.fetchall()
            for user in data:
                    usr = user_data_to_dict(user)
                    user_info.append(usr)
            #print(user_info)
        else:
            #con = pymysql.connect(hostname, username, password, database)
            cur = self.db_conn.cursor()
            cur.execute('SELECT * from self.table_name where id=%s')
            data = cur.fetchall()
            if len(data) >0:
                usr = user_data_to_dict(data[0])
                #print(usr)
            else:
                print("Invalid user")
        cur.close()
        #self.db_conn.commit()
         

    def update_user(self):
        #con = pymysql.connect(hostname, username, password, database)
        cur = self.db_conn.cursor()
        cur.execute('UPDATE self.table_name SET first_name=self.first_name,last_name=last_name,email=self.email,contact_number=self.contact_number, address=self.address, postal_code=self.postal_code, password, user_type=self,user_type where id=%s')
        data = cur.fetchall()
        if len(data) >0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid user")
        cur.close()
        self.db_conn.commit()
        #con.close()

    def delete_user(self):
        #con = pymysql.connect(hostname, username, password, database)
        cur = self.db_conn.cursor()
        cur.execute('DELETE self.table_name where id=%s')
        cur.close()
        self.db_conn.commit()  
        #con.close()      

        

   