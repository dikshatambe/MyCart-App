from utils.dict import user_data_to_dict, unicode_to_str, fill_all_field_in_arg
from utils.dict import raw_data_to_discount_model


class Discount:
    def __init__(self, db_conn=None, discount_id=None, name=None, amount=None, discount=None, discount_type=None, creation_date=None):
        self.table_name = 'discount'
        self.db_conn = db_conn
        self.id = discount_id
        self.name = name
        self.amount = amount
        self.discount = discount
        self.type = discount_type
        self.creation_date = creation_date

    def create_discount(self):
        cur = self.db_conn.cursor()
        cur.execute("""INSERT into {} (name,amount,discount,discount_type) VALUES (\"{}\",{},{},{})""".format(
            self.table_name, self.name, self.amount, self.discount, self.type))
        cur.close()
        self.db_conn.commit()

    def get_discount(self, id=None):
        if id == None:
            cur = self.db_conn.cursor()
            cur.execute("""SELECT * from {}""".format(self.table_name))
            data = cur.fetchall()
            print(data)
            disc_list = []
            for discount in data:
                usr = Discount()
                usr = raw_data_to_discount_model(discount, usr)
                disc_list.append(usr)
            return disc_list
        else:
            cur = self.db_conn.cursor()
            cur.execute(
                """SELECT * from {} where discount_id= {}""".format(self.table_name, self.id))
            data = cur.fetchall()
            if len(data) > 0:
                usr = user_data_to_dict(data[0])
            else:
                print("Invalid discount")
        cur.close()

    def update_discount(self, discount_id, name=None, amount=None, discount=None, discount_type=None):
        cur = self.db_conn.cursor()
        cur.execute("""UPDATE {} SET name=\"{}\", amount={}, discount={},discount_type={} where discount_id={}""".format(
            self.table_name, name, amount, discount, discount_type, discount_id))
        data = cur.fetchall()
        if len(data) <= 0:
            print("Invalid Discount field")
        else:
            print("Discount Updated successfully !")
        cur.close()
        self.db_conn.commit()

    def delete_discount(self, discount_id):
        cur = self.db_conn.cursor()
        cur.execute("""DELETE FROM {} where discount_id={}""".format(
            self.table_name, discount_id))
        print("Successfully deleted discount")
        cur.close()
        self.db_conn.commit()
