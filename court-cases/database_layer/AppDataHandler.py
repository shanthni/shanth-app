from database_layer.DatabaseUtils import DatabaseHandler
import json


class AppLogicDBHandler:
    def __init__(self, config):
        config = json.load(config)
        creds = config["MySQL"]
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], 'casedata')

    def get_county_data(self, state):
        cur = self.db.get_cur()

        qry = f"SELECT GEOdata, county, case_count FROM gis WHERE state = {state}"
        cur.execute(qry)
        geo_data = cur.fetchall()

        qry = f"SELECT latitude, longitude FROM gis_state_coordinates WHERE state = {state}"
        cur.execute(qry)
        coordinates = cur.fetchall()

        qry = f"SELECT meaning FROM state_code WHERE id = {state}"
        cur.execute(qry)
        state = cur.fetchall()

        return geo_data, coordinates, state

    def get_county_cases(self, county):

        cur = self.db.get_cur()

        qry = f""" SELECT cases_data.id as id, defendant_key, county, proceeding_date, prison_time, prob_time, fine, 
                    d2_code.meaning as offense, disposition_code.meaning as disposition
                    FROM (SELECT cases.id as id, defendant_key, county, proceeding_date, prison_time, prob_time, 
                    fine, offense, disposition 
                    FROM termination_data 
                    INNER JOIN (SELECT id, defendant_key, county, proceeding_date
                    FROM case_data WHERE county = {county}) cases ON termination_data.id = cases.id) cases_data 
                    JOIN d2_code ON cases_data.offense = d2_code.id 
                    JOIN disposition_code ON cases_data.disposition = disposition_code.id"""
        cur.execute(qry)
        cases_data = cur.fetchall()

        return cases_data


