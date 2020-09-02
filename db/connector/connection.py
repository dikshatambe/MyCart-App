import pymysql.cursors


def connect_to_db(db , db_host, db_user, db_password):
    con = pymysql.connect(db_host, db_user, db_password, db)
    return con
    