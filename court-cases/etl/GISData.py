from database_layer.GISDataHandler import GISDBHandler
import json


class GISDataLoader:
    def __init__(self, config):
        self.gis_data = json.load(open('./data/gis-data/counties.json'))
        self.DBHandler = GISDBHandler(config)

    def do_load(self):
        self.load_gis_data()
        self.update_county_ids()

    def create_gis_attributes(self):
        attributes = ['county_code', 'county_name', 'GEOid', 'GEOdata']
        self.DBHandler.create_gis_table(attributes)

        print('Created GIS data table\n')
        return attributes

    def load_gis_data(self):
        attributes = self.create_gis_attributes()
        data = []

        for i in self.gis_data["features"]:
            county_idb = i["properties"]["STATE"] + i["properties"]["COUNTY"]
            county_name = i["properties"]["NAME"]
            geo_id = i["properties"]["GEO_ID"]
            geo_data = str(i["geometry"]).replace("'", "\"")

            data.append((county_idb, county_name, geo_id, geo_data))

        self.DBHandler.load_gis_data(attributes, data)
        print('Loaded GIS data\n')

    def update_county_ids(self):
        self.DBHandler.update_county_ids()
        print('Updated county IDs')
