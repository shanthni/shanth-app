import os


class mortality_data_loader:
    def __init__(self):
        self.name = 'mortality data loader'

    def insert_data(self, data, table_name):   
        print(data, table_name)
    
    def create_table(self, table_name, attributes):
        print(table_name, attributes)

    def parse_data(self, file):
        data = []

        with open(file, 'r') as f:
            col = f.readline().strip().replace('"','').split('\t')

            while f.readline():
                row = f.readline().strip().replace('"', '').split('\t')
                if len(row) == len(col):
                    data.append({col[i]: val for i, val in enumerate(row)})
                    
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

                data = [{'year': i['Year Code'], 'state': i['State'], 'deaths': i['Deaths'],
                         'population': i['Population'], 'crude_rate': i['Crude Rate']} for i in data]

                self.insert_data(data, table_name)
    

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

                data = [{'year': i['Year Code'],'deaths': i['Deaths'], 
                         'population': i['Population'], 'crude_rate': i['Crude Rate'],
                         'race': 'Asian or Pacific Islander' if 'Race' not in i else i['Race'],
                         'state': 'None' if 'State' not in i else i['State']} 
                         for i in data]

                self.insert_data(data, table_name)
    
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

                data = [{'year': i['Year Code'],'deaths': i['Deaths'], 'population': i['Population'], 
                         'crude_rate': i['Crude Rate'], 'gender': i['Gender'],
                         'state': 'None' if 'State' not in i else i['State']} 
                         for i in data]

                self.insert_data(data, table_name)


data_loader = mortality_data_loader()
data_loader.load_gender()