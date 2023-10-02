from sas7bdat import SAS7BDAT
from DatabaseUtils import DatabaseHandler
import json


class CDLoader:
    def __init__(self, config):

        config = json.load(config)
        creds = config["MySQL"]
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], 'casedata')

        self.case_attributes = {'circuit': 'VARCHAR(225) NOT NULL',
                                'district': 'VARCHAR(225) NOT NULL', 'office': 'VARCHAR(225) NOT NULL',
                                'docket': 'VARCHAR(225) NOT NULL', 'defendant_no': 'VARCHAR(225) NOT NULL',
                                'defendant_key': 'VARCHAR(225) NOT NULL',
                                'status_code': 'VARCHAR (225)', 'proceeding_date': 'DATE',
                                'proceeding_code': 'VARCHAR (225)', 'f_judge': 'VARCHAR (225)',
                                't_judge': 'VARCHAR (225)', 'f_counsel': 'VARCHAR (225)', 't_counsel': 'VARCHAR (225)',
                                'filing_offense_level': 'VARCHAR (225)', 'filing_offense': 'VARCHAR (225)',
                                'filing_severity': 'VARCHAR (225)', 'county': 'VARCHAR (225)', 'term_date': 'DATE',
                                'term_offense_level': 'VARCHAR (225)', 'term_offense': 'VARCHAR (225)',
                                'term_severity': 'VARCHAR (225)', 'disposition': 'VARCHAR (225)', 'prison_tot': 'FLOAT',
                                'prob_tot': 'FLOAT', 'fine_tot': 'FLOAT'}
        self.create_cases_table()

    def create_cases_table(self):
        cur = self.db.get_cur()

        field_format = (',\n'.join(['{} {}'.format(i, self.case_attributes[i]) for i in self.case_attributes]))

        qry = 'CREATE TABLE IF NOT EXISTS case_data (\n{}\n)'.format(field_format)

        cur.execute(qry)
        self.db.commit()

    def load_cases_staging(self, raw_data):
        cur = self.db.get_cur()
        fields = ', '.join([i for i in self.case_attributes])

        x = 0
        for record in raw_data:

            if record[30] != -8 or record[70] != -8:
                x += 1
                for i in [22, 26, 66, 28, 68, 72]:
                    record[i] = str(int(record[i]))

                row_strings = ['\'{}\''.format(record[i]) for i in [1, 2, 3, 4, 5, 12, 16, 21, 22, 25, 65, 26, 66, 28, 30,
                                                                    31, 52, 60, 68, 70, 71, 72]]

                row_floats = ['{}'.format(record[i]) for i in [73, 75, 78]]

                row = ', '.join(row_strings) + ', ' + ', '.join(row_floats)

                qry = "INSERT INTO case_data ({}) VALUES ({})".format(fields, row)
                cur.execute(qry)

            if x % 10000 == 0 and x >= 10000:
                self.db.commit()
                print("{} records loaded".format(x))

        self.db.commit()

    def load_metadata(self, metadata):
        pass

    def load_mappings(self, mappings):
        pass


credentials = open('../config.json')
data_loader = CDLoader(credentials)

with SAS7BDAT('data/raw-data/cr18to23.sas7bdat', skip_header=True) as reader:
    data_loader.load_cases(reader)
