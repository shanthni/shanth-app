import os
from mortality_data.database_layer.MortalityDataHandler import MortalityDBHandler


class MortalityDataLoader:
    def __init__(self, config):
        self.db_handler = MortalityDBHandler(config)

    def do_load(self):
        self.db_handler.open_connection()

        self.load_state()
        self.load_race()
        self.load_gender()

        self.db_handler.close_connection()

    def insert_data(self, table_name, fields, data):
        self.db_handler.insert(table_name, fields, data)

    def create_table(self, table_name, attributes):
        self.db_handler.create_table(table_name, attributes)

    @staticmethod
    def parse_data(file):
        data = []

        with open(file, 'r') as f:
            col = f.readline().strip().replace('"', '').split('\t')

            row = f.readline()
            while row:
                row = row.strip().replace('"', '').split('\t')
                if len(row) == len(col):
                    data.append({col[i]: val for i, val in enumerate(row)})
                row = f.readline()

        return data

    def load_state(self):
        state_causes = os.listdir('./data/state')

        for cause in state_causes:
            table_name = f'{cause}_state'
            data_files = os.listdir(f'./data/state/{cause}')
            attributes = {'year': 'string', 'state': 'string', 'deaths': 'int',
                          'population': 'int', 'crude_rate': 'float'}
            self.create_table(table_name, attributes)

            for file in data_files:
                data = self.parse_data(f'./data/state/{cause}/{file}')

                data = [(i['Year Code'], None if 'State' not in i else i['State'],
                         i['Deaths'] if i['Deaths'].isnumeric() else None,
                         i['Population'] if i['Population'].isnumeric() else None,
                         i['Crude Rate'] if i['Crude Rate'].replace(".", "").isnumeric() else None)
                        for i in data]

                self.insert_data(table_name, attributes.keys(), data)

    def load_race(self):
        race_causes = os.listdir('./data/race')

        for cause in race_causes:
            table_name = f'{cause}_race'
            data_files = os.listdir(f'./data/race/{cause}')
            attributes = {'year': 'string', 'state': 'string', 'race': 'string', 'deaths': 'int',
                          'population': 'int', 'crude_rate': 'float'}
            self.create_table(table_name, attributes)

            for file in data_files:
                data = self.parse_data(f'./data/race/{cause}/{file}')

                data = [(i['Year Code'], None if 'State' not in i else i['State'],
                         'Asian or Pacific Islander' if 'Race' not in i else i['Race'],
                         i['Deaths'] if i['Deaths'].isnumeric() else None,
                         i['Population'] if i['Population'].isnumeric() else None,
                         i['Crude Rate'] if i['Crude Rate'].replace(".", "").isnumeric() else None)
                        for i in data]

                self.insert_data(table_name, attributes.keys(), data)

    def load_gender(self):
        gender_causes = os.listdir('./data/gender')

        for cause in gender_causes:
            table_name = f'{cause}_gender'
            data_files = os.listdir(f'./data/gender/{cause}')
            attributes = {'year': 'string', 'state': 'string', 'gender': 'string', 'deaths': 'int',
                          'population': 'int', 'crude_rate': 'float'}
            self.create_table(table_name, attributes)

            for file in data_files:
                data = self.parse_data(f'./data/gender/{cause}/{file}')

                data = [(i['Year Code'], None if 'State' not in i else i['State'],
                         None if 'Gender' not in i else i['Gender'],
                         i['Deaths'] if i['Deaths'].isnumeric() else None,
                         i['Population'] if i['Population'].isnumeric() else None,
                         i['Crude Rate'] if i['Crude Rate'].replace(".", "").isnumeric() else None)
                        for i in data]

                self.insert_data(table_name, attributes.keys(), data)
