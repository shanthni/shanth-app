from database_layer.AppDataHandler import AppLogicDBHandler
import json


class AppLogic:
    def __init__(self, config):
        self.DBHandler = AppLogicDBHandler(config)

    def county_data(self, state):
        geo_data, coordinates, name = self.DBHandler.get_county_data(state)

        for i in geo_data:
            i['GEOdata'] = json.loads(i['GEOdata'])
            i['GEOdata']['properties']['case_count'] = str(i['case_count'])
            i['GEOdata']['properties']['county_id'] = int(i['county']) if i['county'] else 0

        county_data = {'name': name[0], 'coordinates': [coordinates[0]['latitude'], coordinates[0]['longitude']],
                       'features': [i['GEOdata'] for i in geo_data]}

        return county_data

    def county_cases(self, county):
        if county == 0:
            return []

        case_data = self.DBHandler.get_county_cases(county)
        return case_data
