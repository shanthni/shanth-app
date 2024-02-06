import csv

from database_layer.GISDataHandler import GISDBHandler
import json


class GISDataLoader:
    def __init__(self, config):
        self.gis_data = json.load(open('./data/gis-data/counties.json'))
        self.coordinate_data = json.load(open('./data/gis-data/state_coordinates.json'))
        self.DBHandler = GISDBHandler(config)

    def do_load(self):
        self.load_gis_data()
        self.update_gis_ids()
        self.load_center_coordinates()

    def load_gis_data(self):

        attributes = ['state_code', 'county_code', 'county_name', 'GEOid', 'GEOdata']
        data = []

        for i in self.gis_data["features"]:
            state_idb = i["properties"]["STATE"]
            county_idb = i["properties"]["STATE"] + i["properties"]["COUNTY"]
            county_name = i["properties"]["NAME"]
            geo_id = i["properties"]["GEO_ID"]
            geo_data = str(json.dumps(i))

            data.append((state_idb, county_idb, county_name, geo_id, geo_data))

        self.DBHandler.load_gis_data(attributes, data)
        print('Loaded GIS data\n')

    def load_center_coordinates(self):
        attributes = ['state_name', 'latitude', 'longitude']

        data = []

        for i in self.coordinate_data:
            state_name = i["state"]
            lat = float(i["latitude"])
            long = float(i["longitude"])

            data.append((state_name, lat, long))

        self.DBHandler.load_coordinate_data(attributes, data)
        print('Loaded center coordinates for each state\n')

        self.DBHandler.update_coordinate_ids()
        print('Updated state ids\n')

    def update_gis_ids(self):
        self.DBHandler.update_gis_ids()
        print('Updated county and state IDs')

        self.DBHandler.get_case_counts()
        print('Added case counts for each county')
