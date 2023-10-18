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
        except pymysql.Error as e:
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
        con = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur = con.cursor()
            qry = "DROP DATABASE {}".format(db)
            cur.execute(qry)

    def create_table(self, name, attributes):
        cur = self.get_cur()

        field_format = (',\n'.join(['{} {}'.format(i, attributes[i]) for i in attributes]))

        qry = 'CREATE TABLE IF NOT EXISTS {} (\n{}\n)'.format(name, field_format)

        cur.execute(qry)
        self.commit()

    def get_con(self):
        return self.con

    def get_cur(self):
        cur = self.con.cursor()
        return cur

    @staticmethod
    def execute(self, cur, qry):
        cur.execute(qry)

    def commit(self):
        self.con.commit()

    @staticmethod
    def fetch_all(self, cur):
        return cur.fetchall()
