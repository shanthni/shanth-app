from database_layer.DatabaseUtils import DatabaseHandler
import json


class AppLogicDBHandler:
    def __init__(self, config):
        config = json.load(config)
        creds = config["MySQL"]
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], 'casedata')

    def get_county_data(self, state):
        cur = self.db.get_cur()

        qry = f"SELECT GEOdata FROM gis WHERE state = {state}"
        cur.execute(qry)
        geo_data = cur.fetchall()

        qry = f"SELECT latitude, longitude FROM gis_state_coordinates WHERE state = {state}"
        cur.execute(qry)
        coordinates = cur.fetchall()

        qry = f"SELECT meaning FROM state_code WHERE id = {state}"
        cur.execute(qry)
        state = cur.fetchall()

        return geo_data, coordinates, state

