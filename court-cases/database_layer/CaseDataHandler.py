from database_layer.DatabaseUtils import DatabaseHandler
import json


class CaseDBHandler:
    def __init__(self, config):
        config = json.load(config)
        creds = config["MySQL"]
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], 'casedata')

    def create_staging_table(self, column_names, column_types):
        cur = self.db.get_cur()

        fields = dict()
        fields['id'] = 'INT AUTO_INCREMENT PRIMARY KEY'
        for i in range(0, len(column_names)):
            column_name = column_names[i]
            if column_types[i] == 'string':
                fields[column_name] = "VARCHAR (50)"
            elif column_types[i] == 'number':
                fields[column_name] = "FLOAT"
            else:
                print(column_types[i])

            if "DATE" in column_name:
                fields[column_name] = "DATE"

        self.db.create_table('staging', fields)

        qry = "CREATE INDEX staging_DEFLGKY ON staging (DEFLGKY_)"
        cur.execute(qry)
        self.db.commit()

    def load_staging_data(self, fields, data):

        cur = self.db.get_cur()
        qry = 'INSERT INTO staging ({}) VALUES({})'.format(', '.join(fields),
                                                           ', '.join(['%s'] * (len(fields))))

        cur.executemany(qry, data)
        self.db.commit()

    def load_mapping(self, name, attributes, data):

        cur = self.db.get_cur()

        attributes = {
            code: 'VARCHAR (225)' for code in attributes
        }
        attributes['id'] = 'INT AUTO_INCREMENT NOT NULL PRIMARY KEY'
        self.db.create_table(name, attributes)

        qry = "INSERT INTO {} ({}) VALUES ({})".format(name,
                                                       ', '.join([i for i in attributes.keys() if i != 'id']),
                                                       ', '.join(['%s'] * (len(attributes) - 1)))

        cur.executemany(qry, data)
        self.db.commit()

    def find_unique_ids(self):
        cur = self.db.get_cur()

        qry = """CREATE TABLE IF NOT EXISTS case_ids SELECT staging.id AS id FROM 
                (SELECT MIN(id) id FROM casedata.staging GROUP BY DEFLGKY_) a LEFT JOIN staging ON a.id = staging.id"""

        cur.execute(qry)
        self.db.commit()

    def load_cases(self, attributes):

        cur = self.db.get_cur()

        fields = ', '.join(['staging.' + i[1] + ' AS ' + i[0] for i in attributes])

        qry = """CREATE TABLE case_data SELECT {} FROM case_ids 
                        LEFT JOIN staging ON case_ids.id = staging.id""".format(fields)

        cur.execute(qry)

        qry = f"CREATE INDEX county_code ON case_data (countyIDB)"
        cur.execute(qry)

        self.db.commit()
        print('Created table of non-duplicated cases\n')

    def load_offenses(self, attributes, offense_type, offense_abbr):

        cur = self.db.get_cur()

        qry = "CREATE TABLE {} SELECT * FROM (\n".format(offense_type + '_data')
        selects = []

        for i in range(0, 5):
            order = i + 1

            order_attributes = [[i[0], i[1] + str(order) + '_'] if i[0] != 'id' else [i[0], i[1]] for i in attributes]

            fields = ', '.join(['staging.' + i[1] + ' AS ' + i[0] for i in order_attributes])
            fields += ', {} AS offense_order'.format(order)

            selects.append("SELECT {} FROM\ncase_ids LEFT JOIN staging ON case_ids.id = staging.id WHERE "
                           "staging.D2{}OFFCD{}_ != '-8'".format(fields, offense_abbr, order))

        qry += '\nUNION ALL\n'.join(selects) + ') cases'

        cur.execute(qry)

        qry = f"CREATE INDEX d2_code ON {offense_type}_data (offenseIDB)"
        cur.execute(qry)

        self.db.commit()

    def map_data(self, mappings):
        cur = self.db.get_cur()

        for table in mappings.keys():
            for column in mappings[table].keys():
                new_column = column[:-3]

                qry = f'ALTER TABLE {table} ADD COLUMN {new_column} INT'
                cur.execute(qry)

                qry = f"""UPDATE {table} INNER JOIN {mappings[table][column]} ON 
                        {table}.{column} = {mappings[table][column]}.IDB_id SET 
                        {table}.{new_column} = {mappings[table][column]}.id"""
                cur.execute(qry)

                qry = f'ALTER TABLE {table} DROP COLUMN {column}'
                cur.execute(qry)

                self.db.commit()
                print(f"Updated {new_column}")
