from utils.dict import user_data_to_dict, unicode_to_str, fill_all_field_in_arg
from utils.dict import raw_data_to_product_model


class Products:
    def __init__(self, db_conn=None, product_id=None, product_name=None, category_id=None, info=None, color=None, product_size=None, price=None, creation_date=None):
        self.table_name = 'products'
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
        cur.execute("""INSERT into {} (product_name, category_id, info, color, product_size, price) VALUES (\"{}\",{},\"{}\",\"{}\",{},{})""".format(
            self.table_name, self.product_name, self.category_id, self.info, self.color, self.product_size, self.price))
        cur.close()
        self.db_conn.commit()

    def get_product(self, product_id=None):
        if product_id == None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {}""".format(self.table_name))
            data = cur.fetchall()
            print(data)
            prod_list = []
            for user in data:
                usr = Products()
                usr = raw_data_to_product_model(user, usr)
                prod_list.append(usr)
            return prod_list
        else:
            cur = self.db_conn.cursor()
            cur.execute(
                """SELECT * from {} where product_id= {}""".format(self.table_name, self.id))
            data = cur.fetchall()
            if len(data) > 0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid product")
        cur.close()

    def update_product(self, product_name=None, category_id=None, info=None, color=None, product_size=None, price=None):
        cur = self.db_conn.cursor()

        cur.execute("""UPDATE {} SET product_name=\"{}\",category_id={}, info=\"{}\", color=\"{}\", product_size={}, price={} where product_id={}""".format(
            self.table_name, product_name, category_id, info, color, product_size, price, product_id))
        data = cur.fetchall()
        if len(data) <= 0:
            print("Invalid product")
        else:
            print("Successfully Updated")
        cur.close()
        self.db_conn.commit()

    def delete_product(self, product_id):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE {} where product_id={}""".format(
            self.table_name, product_id))
        print("Product deleted successfully")
        cur.close()
        self.db_conn.commit()
