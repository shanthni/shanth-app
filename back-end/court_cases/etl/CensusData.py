import csv

from court_cases.database_layer.CensusDataHandler import CensusDBHandler
import json


class CensusDataLoader:
    def __init__(self, config):
        self.income_data = open('./data/census-data/Unemployment.csv')
        self.population_data = open('./data/census-data/PopulationEstimates.csv')
        self.DBHandler = CensusDBHandler(config)

    def do_load(self):
        self.DBHandler.open_connection()

        self.load_population_table()
        self.load_income_table()
        self.merge_tables()

        self.DBHandler.close_connection()
        print("Finished loading census data\n")

    def load_population_table(self):
        data = list(self.population_data)[1:]
        population_data = []

        for record in data:
            record = [i.replace(',', '').replace('"', '') for i in record.split('","')]
            county = record[0]
            population = int(record[8]) if record[8] != '' else record[10] if record[10] != '' else 0
            population_data.append((county, population))

        self.DBHandler.load_census_data('census_population', population_data, ['county', 'population'])

    def load_income_table(self):
        data = list(self.income_data)[1:]
        income_data = []

        for record in data:
            record = [i.replace(',', '').replace('"', '') for i in record.split('","')]
            county = record[0]
            income = int(record[-2]) if record[-2] != '' else 0
            income_data.append((county, income))

        self.DBHandler.load_census_data('census_income', income_data, ['county', 'income'])

    def merge_tables(self):
        self.DBHandler.merge_tables()
        print('Merged census data\n')
