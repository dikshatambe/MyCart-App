from utils.dict import user_data_to_dict, unicode_to_str, fill_all_field_in_arg
from utils.dict import raw_data_to_category_model


class Category:
    def __init__(self, db_conn=None, category_id=None, cname=None, info=None, is_deleted=None, creation_date=None):
        self.table_name = 'category'
        self.db_conn = db_conn
        self.id = category_id
        self.cname = cname
        self.info = info
        self.is_deleted = is_deleted
        self.creation_date = creation_date

    def create_category(self):
        cur = self.db_conn.cursor()
        cur.execute("""INSERT into {} (cname, info, is_deleted) VALUES (\"{}\",\"{}\",{})""".format(
            self.table_name, self.cname, self.info, self.is_deleted))
        cur.close()
        self.db_conn.commit()

    def get_category(self, id=None):
        if id == None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {}""".format(self.table_name))
            data = cur.fetchall()
            print(data)
            cat_list = []
            for user in data:
                usr = Category()
                usr = raw_data_to_category_model(user, usr)
                cat_list.append(usr)
            return cat_list
        else:
            cur = self.db_conn.cursor()
            cur.execute(
                """SELECT * from {} where category_id= {}""".format(self.table_name, self.id))
            data = cur.fetchall()
            if len(data) > 0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid category")
        cur.close()

    def update_category(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE {} SET category_id={}, cname={}, info={}, is_deleted={}, creation_date={} where categoy_id={}""".format(
            self.table_name,  self.id, self.cname, self.info, self.is_deleted, self.creation_date, id))
        data = cur.fetchall()
        if len(data) > 0:
            usr = user_data_to_dict(data[0])
        else:
            print("Invalid category")
        cur.close()
        self.db_conn.commit()

    def delete_category(self, id=None):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE {} where category_id={} """.format(
            self.table_name, self.id))
        cur.close()
        self.db_conn.commit()
