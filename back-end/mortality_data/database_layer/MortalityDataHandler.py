from Utils.DatabaseUtils import DatabaseHandler


class MortalityDBHandler:
    def __init__(self, config):
        self.db = DatabaseHandler(config['host'], config['user'], config['password'], config['db'])

    def create_table(self, table_name, attributes):
        types = {'string': 'VARCHAR (225)', 'int': 'INT', 'float': 'DECIMAL(10,2)'}
        attributes = {i: types[attributes[i]] for i in attributes}
        attributes['id'] = 'INT AUTO_INCREMENT PRIMARY KEY'

        self.db.create_table(table_name, attributes)

    def insert(self, table, fields, data):
        self.db.bulk_insert(table, fields, data)

    def open_connection(self):
        self.db.connect_to_db()

    def close_connection(self):
        self.db.close_connection()
