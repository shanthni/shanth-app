import pymysql


class DatabaseHandler:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

        self.con = None
        self.cur = None

    def connect_to_db(self):
        try:
            self.con = pymysql.connect(host=self.host,
                                       user=self.user,
                                       password=self.password,
                                       db=self.db,
                                       cursorclass=pymysql.cursors.DictCursor,
                                       charset='utf8mb4')
            self.cur = self.con.cursor()
            print(f"Connected to db: {self.db}\n")

        except pymysql.Error as e:

            self.con = None
            self.cur = None

            print(f"Failed to connect to db: {self.db}\n")

    def create_database(self):
        con = pymysql.connect(host=self.host,
                              user=self.user,
                              password=self.password,
                              cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur = con.cursor()
            qry = "CREATE DATABASE {} CHARACTER SET='{}' COLLATE='{}'".format(self.db, "utf8mb4", "utf8mb4_general_ci")
            cur.execute(qry)
            cur.close()

        return con

    def drop_database(self):
        con = pymysql.connect(host=self.host,
                              user=self.user,
                              password=self.password,
                              cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur = con.cursor()
            qry = "DROP DATABASE {}".format(self.db)
            cur.execute(qry)

    def create_table(self, name, attributes):

        field_format = (',\n'.join(['{} {}'.format(i, attributes[i]) for i in attributes]))

        qry = 'CREATE TABLE IF NOT EXISTS {} (\n{}\n)'.format(name, field_format)

        self.execute(qry)
        self.commit()

    def bulk_insert(self, table, fields, values):

        qry = f"""INSERT INTO {table} ({", ".join([i for i in fields])}) VALUES
                       ({", ".join(["%s"] * len(fields))})"""

        self.executemany(qry, values)

        self.commit()

    def get_con(self):
        if not self.con:
            self.connect_to_db()

        return self.con

    def get_cur(self):
        if not self.con:
            self.connect_to_db()

        return self.cur

    def close_connection(self):
        self.cur.close()
        self.con.close()

        self.con = None
        self.cur = None

        print(f"Closed db connection to: {self.db}\n")

    def execute(self, qry):
        if not self.cur:
            if not self.connect_to_db():
                return

        self.cur.execute(qry)

    def executemany(self, qry, values):
        if not self.cur:
            if not self.connect_to_db():
                return

        self.cur.executemany(qry, values)

    def commit(self):
        if not self.con:
            if not self.connect_to_db():
                return

        self.con.commit()

    def fetchall(self):
        if not self.cur:
            if not self.connect_to_db():
                return None

        return self.cur.fetchall()
