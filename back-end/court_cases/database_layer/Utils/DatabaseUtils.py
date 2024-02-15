import pymysql


class DatabaseHandler:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

        try:
            self.con = self.connect_to_db(host, user, password, db)
        except pymysql.Error as e:
            self.con = self.create_database(host, user, password, db)

        self.cur = self.con.cursor()

        print(f"Connected to database: {db}")

    @staticmethod
    def connect_to_db(host, user, password, db):
        return pymysql.connect(host=host,
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
            cur.close()

        return con

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

    def bulk_insert(self, table, fields, values):
        cur = self.get_cur()

        qry = f"""INSERT INTO {table} ({", ".join([i for i in fields])}) VALUES
                       ({", ".join(["%s"] * len(fields))})"""

        cur.executemany(qry, values)

        self.commit()

    def get_con(self):
        return self.con

    def get_cur(self):
        if self.con:
            return self.cur

        else:
            self.con = self.connect_to_db(self.host, self.user, self.password, self.db)
            self.cur = self.con.cursor()

            return self.cur

    def close_connection(self):
        self.cur.close()
        self.con.close()

        self.con = None
        self.cur = None

    @staticmethod
    def execute(cur, qry):
        cur.execute(qry)

    def commit(self):
        self.con.commit()

    @staticmethod
    def fetch_all(self, cur):
        return cur.fetchall()
