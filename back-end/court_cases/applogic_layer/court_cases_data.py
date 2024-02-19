from court_cases.database_layer.AppDataHandler import AppLogicDBHandler
import json


class AppLogic:
    def __init__(self, config):
        self.DBHandler = AppLogicDBHandler(config)

    @staticmethod
    def process_geo_data(data, center):
        max_ratio = float(max([i['case_ratio'] for i in data if i['case_ratio']]))
        max_ratio = max_ratio if max_ratio < 1 else 1

        for i in data:
            i['GEOdata'] = json.loads(i['GEOdata'])

            i['case_ratio'] = (float(i['case_ratio']) if i['case_ratio'] < 1 else 1) if i['case_ratio'] else 0
            i['GEOdata']['properties']['color'] = i['case_ratio']/max_ratio
            i['county_name'] = i['GEOdata']['properties']['NAME']

        geo_data = {'features': [i['GEOdata'] for i in data],
                    'coordinates': [center[0]['latitude'], center[0]['longitude']]}

        census_data = [{'county_name': i['county_name'], 'population': i['population'], 'income': i['income'],
                        'case_ratio': i['case_ratio']} for i in data]

        return geo_data, census_data

    def state_level_data(self, state):
        if state < 1 or state > 51:
            return None

        self.DBHandler.open_connection()

        geo_data = self.DBHandler.get_geo_data(state)
        coordinates = self.DBHandler.get_state_center(state)
        offense_data = self.DBHandler.get_state_offense_data(state)
        name = self.DBHandler.get_state_name(state)
        stats = self.DBHandler.get_state_stats(state)

        self.DBHandler.close_connection()

        geo_data, census_data = self.process_geo_data(geo_data, coordinates)

        state_data = {'geo_data': geo_data, 'census_data': census_data, 'offense_data': offense_data,
                      'stats': [{i['title']: i['stat'] for i in stats}], 'state': name[0]['meaning']}

        return state_data

    def county_level_data(self, county):
        if county < 1 or county > 3198:
            return None

        self.DBHandler.open_connection()

        case_data = self.DBHandler.get_county_data(county)
        county_name = self.DBHandler.get_county_name(county)

        self.DBHandler.close_connection()

        for i in range(0, len(case_data)):
            case_data[i]['id'] = i + 1

        return {'name': county_name[0]['meaning'], 'data': case_data}
