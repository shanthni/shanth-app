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

    def create_staging_table(self, column_names, column_types):
        fields = dict()

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

        self.db.create_table('staging', fields)
        return fields

    def load_cases_staging(self, raw_data):

        fields = self.create_staging_table(raw_data.column_names, raw_data.column_types)

        cur = self.db.get_cur()
        # type_format = ['%s' if fields[i] == 'FLOAT' else '\'%s\'' for i in fields.keys()]
        qry = 'INSERT INTO staging ({}) VALUES({})'.format(', '.join(fields.keys()),
                                                           ', '.join(['%s'] * len(fields)))

        x = 0
        data = []
        for record in raw_data:
            x += 1
            data.append(tuple(record))

            if x != 0 and x % 100000 == 0:
                cur.executemany(qry, data)
                self.db.commit()
                print("loaded {} records".format(x))
                data = []

        cur.executemany(qry, data)
        self.db.commit()
        print("loaded {} records, all done!".format(x))

    def load_metadata(self, metadata):
        pass

    def load_mappings(self, mappings):

        cur = self.db.get_cur()

        for file in mappings:
            with open('./data/mappings/' + file, encoding="utf-8", mode='r') as f:
                codes = csv.reader(f)
                codes = list(codes)

                attributes = {'id': 'INT AUTO_INCREMENT NOT NULL PRIMARY KEY'}
                for i in codes[0]:
                    attributes[i] = 'VARCHAR (225)'

                self.db.create_table(file[0:-4], attributes)

                qry = "INSERT INTO {} ({}) VALUES ({})".format(file[0:-4],
                                                               ', '.join([i for i in attributes.keys() if i != 'id']),
                                                               ', '.join(['%s'] * (len(attributes) - 1)))
                data = []
                for c in codes[1:]:
                    data.append(tuple(c))

                cur.executemany(qry, data)
                self.db.commit()
                print("Loaded Mapping for {}".format(file))


credentials = open('../config.json')
data_loader = CDLoader(credentials)

# Load Raw Data
''' with SAS7BDAT('data/raw-data/cr18to23.sas7bdat', skip_header=True) as reader:
    data_loader.load_cases_staging(reader) '''

# Load Mappings
data_loader.load_mappings(os.listdir('./data/mappings'))
