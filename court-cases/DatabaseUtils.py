import pymysql


class DatabaseHandler:
    def __init__(self, host, user, password, db):
        try:
            self.con = pymysql.connect(host=host,
                                       user=user,
                                       password=password,
                                       db=db,
                                       cursorclass=pymysql.cursors.DictCursor,
                                       charset='utf8mb4')
        except:
            DatabaseHandler.create_database(host, user, password, db)
            self.con = pymysql.connect(host=host,
                                       user=user,
                                       password=password,
                                       db=db,
                                       cursorclass=pymysql.cursors.DictCursor,
                                       charset='utf8mb4')

    @staticmethod
    def create_database(host, user, password, db):
        con = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur = con.cursor()
            qry = "CREATE DATABASE {} CHARACTER SET='{}' COLLATE='{}'".format(db, "utf8mb4", "utf8mb4_general_ci")
            cur.execute(qry)

    @staticmethod
    def drop_database(host, user, password, db):
        try:
            con = pymysql.connect(host=host,
                                  user=user,
                                  password=password,
                                  cursorclass=pymysql.cursors.DictCursor)
            with con:
                cur = con.cursor()
                qry = "DROP DATABASE {}".format(db)
                cur.execute(qry)
        except:
            print("There was an error Dropping Database")

    def get_con(self):
        return self.con

    def get_cur(self):
        cur = self.con.cursor()
        return cur

    def execute(self, cur, qry):
        cur.execute(qry)

    def commit(self):
        self.con.commit()

    def fetch_all(self, cur):
        return cur.fetchall()