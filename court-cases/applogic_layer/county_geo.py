from database_layer.AppDataHandler import AppLogicDBHandler
import json

class AppLogic:
    def __init__(self, config):
        self.DBHandler = AppLogicDBHandler(config)

    def county_data(self, state):
        geo_data, coordinates, name = self.DBHandler.get_county_data(state)
        county_data = {'name': name[0], 'coordinates': [coordinates[0]['latitude'], coordinates[0]['longitude']],
                       'features': [json.loads(i['GEOdata']) for i in geo_data]}

        return county_data
