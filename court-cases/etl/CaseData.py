import csv
import os
import json
from sas7bdat import SAS7BDAT
from database_layer.CaseDataHandler import CaseDBHandler


class CDLoader:
    def __init__(self, config):
        self.raw_data = SAS7BDAT('./data/cases-data/raw-data/cr18to23.sas7bdat', skip_header=True)

        self.termination_metadata = open('./data/cases-data/metadata/metadata-termination.csv', encoding="utf-8")
        self.filing_metadata = open('./data/cases-data/metadata/metadata-filing.csv', encoding="utf-8")
        self.case_metadata = open('./data/cases-data/metadata/metadata-case.csv', encoding="utf-8")

        self.mapped_fields = open('./data/cases-data/metadata/mappings.json')
        self.mappings = os.listdir('./data/cases-data/mappings')

        self.DBHandler = CaseDBHandler(config)

    def do_load(self):

        self.load_staging_data()

        self.load_mappings()

        self.load_case_data()
        self.load_filing_data()
        self.load_termination_data()

        self.load_mappings()

    def create_staging_table(self):
        fields = [str(i)[2:-1] + '_' for i in self.raw_data.column_names]
        types = self.raw_data.column_types

        for i in range(0, 5):
            order = str(i + 1)
            fields.extend(['f_sev_pris' + order + '_', 'f_sev_off' + order + '_', 'f_sev_fine' + order + '_',
                           't_sev_pris' + order + '_', 't_sev_off' + order + '_', 't_sev_fine' + order + '_'])

        fields.append('prison_tc_')
        fields.extend(['pris_tc' + str(i + 1) + '_' for i in range(0, 5)])

        types.extend(['string'] * (len(fields) - len(types)))

        self.DBHandler.create_staging_table(fields, types)
        print('Created Staging Table\n')
        return fields

    def load_staging_data(self):

        fields = self.create_staging_table()
        data = []

        x = 0
        for record in self.raw_data:
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
                self.DBHandler.load_staging_data(fields, data)
                data = []
                print(f'Loaded {x}')

        self.DBHandler.load_staging_data(fields, data)

        print('Finished loading staging data\n')

    def load_mappings(self):

        for file in self.mappings:
            with open('./data/cases-data/mappings/' + file, encoding="utf-8", mode='r') as f:
                codes = list(csv.reader(f))
                attributes = codes[0]
                data = [tuple(c) for c in codes[1:]]
                name = file[0:-4]

                self.DBHandler.load_mapping(name, attributes, data)
        print('Finished Loading Mappings\n')

    def load_case_data(self):

        attributes = list(csv.reader(self.case_metadata))[1:]

        self.DBHandler.find_unique_ids()
        self.DBHandler.load_cases(attributes)
        print('Loaded case data\n')

    def load_filing_data(self):
        attributes = list(csv.reader(self.filing_metadata))[1:]
        offense_type = 'filing'
        abbr = 'F'
        self.DBHandler.load_offenses(attributes, offense_type, abbr)
        print('Loaded filing data\n')

    def load_termination_data(self):
        attributes = list(csv.reader(self.termination_metadata))[1:]
        offense_type = 'termination'
        abbr = 'T'
        self.DBHandler.load_offenses(attributes, offense_type, abbr)
        print('Loaded termination data\n')

    def map_data(self):
        mappings = json.load(self.mapped_fields)
        self.DBHandler.map_data(mappings)

