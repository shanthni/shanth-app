import csv

from database_layer.GISDataHandler import GISDBHandler
import json


class GISDataLoader:
    def __init__(self, config):
        self.gis_data = json.load(open('./data/gis-data/counties.json'))
        self.DBHandler = GISDBHandler(config)

    def do_load(self):
        self.load_gis_data()
        self.load_state_mappings()
        self.update_county_ids()

    def create_gis_attributes(self):
        attributes = ['state_code', 'county_code', 'county_name', 'GEOid', 'GEOdata']
        self.DBHandler.create_gis_table(attributes)

        print('Created GIS data table\n')
        return attributes

    def load_gis_data(self):
        attributes = self.create_gis_attributes()
        data = []

        for i in self.gis_data["features"]:
            state_idb = i["properties"]["STATE"]
            county_idb = i["properties"]["STATE"] + i["properties"]["COUNTY"]
            county_name = i["properties"]["NAME"]
            geo_id = i["properties"]["GEO_ID"]
            geo_data = str(i["geometry"]).replace("'", "\"")

            data.append((state_idb, county_idb, county_name, geo_id, geo_data))

        self.DBHandler.load_gis_data(attributes, data)
        print('Loaded GIS data\n')

    def load_state_mappings(self):

        with open('./data/gis-data/mappings/state_code.csv', encoding="utf-8", mode='r') as f:
            codes = list(csv.reader(f))
            attributes = codes[0]
            data = [tuple(c) for c in codes[1:]]

            self.DBHandler.load_state_mapping(attributes, data)
        print('Finished Loading State Mapping\n')

    def update_county_ids(self):
        self.DBHandler.update_county_ids()
        print('Updated county and state IDs')
