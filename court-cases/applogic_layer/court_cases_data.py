from database_layer.AppDataHandler import AppLogicDBHandler
import json


class AppLogic:
    def __init__(self, config):
        self.DBHandler = AppLogicDBHandler(config)

    def process_geo_data(self, geo_data, max_ratio):

        max_ratio = float(max_ratio[0]['perc']) if float(max_ratio[0]['perc']) < 1 else 1

        for i in geo_data:
            i['GEOdata'] = json.loads(i['GEOdata'])
            i['GEOdata']['properties']['county_id'] = int(i['county'] if i['county'] else 0)

            case_count = i['case_count'] if i['case_count'] else 0
            population = i['population'] if i['population'] else 0
            ratio = (case_count / population) / max_ratio if population > 0 else 0

            i['GEOdata']['properties']['color'], i['case_ratio'] = (ratio, ratio) if ratio < 1 else (1, 1)
            i['county_name'] = i['GEOdata']['properties']['NAME']

        return geo_data

    def state_level_data(self, state):
        geo_data = self.DBHandler.get_geo_data(state)
        max_ratio = self.DBHandler.get_max_ratio_state(state)
        coordinates = self.DBHandler.get_state_center(state)
        offense_data = self.DBHandler.get_state_offense_data(state)
        name = self.DBHandler.get_state_name(state)

        geo_data = self.process_geo_data(geo_data, max_ratio)

        state_data = {'geo_data': {'features': [i['GEOdata'] for i in geo_data],
                                   'coordinates': [coordinates[0]['latitude'], coordinates[0]['longitude']]},
                      'census_data': [{'county_name': i['county_name'], 'population': i['population'],
                                       'income': i['income'], 'case_ratio': i['case_ratio']}
                                      for i in geo_data],
                      'offense_data': offense_data[:10],
                      'state': name[0]['meaning']}

        return state_data

    def county_level_data(self, county):
        if county == 0:
            return []

        case_data = self.DBHandler.get_county_data(county)
        county_name = self.DBHandler.get_county_name(county)

        for i in range(0, len(case_data)):
            case_data[i]['id'] = i + 1

        return {'name': county_name[0]['meaning'], 'data': case_data}
