from sas7bdat import SAS7BDAT
from DatabaseUtils import DatabaseHandler
import json
import os
import csv


class CDLoader:
    def __init__(self, config):
        config = json.load(config)
        creds = config["MySQL"]
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], 'casedata')

    def do_load(self):
        print('Starting data load!\n')
        self.do_load_raw_data()

        self.do_load_mappings()

        self.do_clean_data()

        self.do_map_data()
        print('Finished data load!')

    def do_load_raw_data(self):
        with SAS7BDAT('data/raw-data/cr18to23.sas7bdat', skip_header=True) as reader:
            self.load_cases_staging(reader)

    def do_load_mappings(self):
        self.load_mappings(os.listdir('./data/mappings'))

    def do_clean_data(self):
        self.load_cases('./data/metadata/metadata-case.csv')
        self.load_offenses('./data/metadata/metadata-filing.csv', 'filing')
        self.load_offenses('./data/metadata/metadata-termination.csv', 'termination')

    def do_map_data(self):
        mapping = open('data/metadata/mappings.json')
        self.map_data(mapping)

    def create_staging_table(self, column_names, column_types):
        fields = dict()
        fields['id'] = 'INT AUTO_INCREMENT PRIMARY KEY'
        for i in range(0, len(column_names)):
            column_name = str(column_names[i])[2:-1] + '_'

            if column_types[i] == 'string':
                fields[column_name] = "VARCHAR (50)"
            elif column_types[i] == 'number':
                fields[column_name] = "FLOAT"
            else:
                print(column_types[i])

            if "DATE" in column_name:
                fields[column_name] = "DATE"

        new_fields = []
        for i in range(0, 5):
            order = str(i + 1)
            new_fields.extend(['f_sev_pris' + order + '_', 'f_sev_off' + order + '_', 'f_sev_fine' + order + '_',
                               't_sev_pris' + order + '_', 't_sev_off' + order + '_', 't_sev_fine' + order + '_'])

        new_fields.append('prison_tc_')
        new_fields.extend(['pris_tc' + str(i + 1) + '_' for i in range(0, 5)])

        for i in new_fields:
            fields[i] = 'VARCHAR (50)'

        self.db.create_table('staging', fields)

        print('Staging Table Created\n')
        return fields

    def load_cases_staging(self, raw_data):

        fields = self.create_staging_table(raw_data.column_names, raw_data.column_types)

        cur = self.db.get_cur()

        qry = 'INSERT INTO staging ({}) VALUES({})'.format(', '.join([i for i in fields.keys() if i != 'id']),
                                                           ', '.join(['%s'] * (len(fields) - 1)))

        x = 0
        data = []
        for record in raw_data:
            x += 1

            for i in [31, 71, 36, 83, 41, 95, 46, 107, 51, 119]:
                if record[i] != '-8':
                    record.extend([record[i][0], record[i][1], record[i][2]])
                else:
                    record.extend([None, None, None])

            for i in [127, 73, 85, 97, 109, 121]:
                if record[i] < 0:
                    record.append(str(int(record[i])))
                    record[i] = None
                else:
                    record.append(None)

            data.append(tuple(record))

            if x != 0 and x % 100000 == 0:
                cur.executemany(qry, data)
                self.db.commit()
                print("Loaded {} records".format(x))
                data = []

        cur.executemany(qry, data)
        self.db.commit()
        print("Loaded {} records, all done!\n".format(x))

        qry = "CREATE INDEX staging_DEFLGKY ON staging (DEFLGKY_)"
        cur.execute(qry)

        self.db.commit()

    def load_mappings(self, mappings):

        cur = self.db.get_cur()

        for file in mappings:
            with open('./data/mappings/' + file, encoding="utf-8", mode='r') as f:
                codes = csv.reader(f)
                codes = list(codes)

                attributes = {
                    code: 'VARCHAR (225)' for code in codes[0]
                }
                attributes['id'] = 'INT AUTO_INCREMENT NOT NULL PRIMARY KEY'

                self.db.create_table(file[0:-4], attributes)

                qry = "INSERT INTO {} ({}) VALUES ({})".format(file[0:-4],
                                                               ', '.join([i for i in attributes.keys() if i != 'id']),
                                                               ', '.join(['%s'] * (len(attributes) - 1)))
                data = [tuple(c) for c in codes[1:]]

                cur.executemany(qry, data)
                self.db.commit()
                print("Loaded Mapping for {}".format(file))
        print('\n')

    def find_unique_ids(self):
        cur = self.db.get_cur()

        qry = """CREATE TABLE IF NOT EXISTS case_ids SELECT staging.id AS id FROM 
                (SELECT MIN(id) id FROM casedata.staging GROUP BY DEFLGKY_) a LEFT JOIN staging ON a.id = staging.id"""

        cur.execute(qry)
        self.db.commit()
        print('Created table of ids for non-duplicated cases')

    def load_cases(self, case_metadata):
        self.find_unique_ids()

        cur = self.db.get_cur()

        with open(case_metadata, encoding="utf-8", mode='r') as f:
            attributes = list(csv.reader(f))[1:]

        fields = ', '.join(['staging.' + i[1] + ' AS ' + i[0] for i in attributes])

        qry = """CREATE TABLE case_data SELECT {} FROM case_ids 
                        LEFT JOIN staging ON case_ids.id = staging.id""".format(fields)

        cur.execute(qry)

        qry = f"CREATE INDEX county_code ON case_data (countyIDB)"
        cur.execute(qry)

        self.db.commit()
        print('Created table of non-duplicated cases\n')

    def load_offenses(self, offense_metadata, offense_type):

        cur = self.db.get_cur()

        offense_abbr = "T"
        if offense_type == 'filing':
            offense_abbr = "F"

        with open(offense_metadata, encoding="utf-8", mode='r') as f:
            attributes = list(csv.reader(f))[1:]

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
        print('Created table of {} offenses\n'.format(offense_type))

    def map_data(self, mappings):
        cur = self.db.get_cur()
        mappings = json.load(mappings)

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
                print(f'Mapped column {column} in {table}')

            print(f'Mapped data for {table}\n')


credentials = open('../config.json')
data_loader = CDLoader(credentials)
data_loader.do_load()


