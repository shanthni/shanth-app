from database_layer.DatabaseUtils import DatabaseHandler
import json


class AppLogicDBHandler:
    def __init__(self, config):
        config = json.load(config)
        creds = config["MySQL"]
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], 'casedata')

    def get_geo_data(self, state):
        cur = self.db.get_cur()

        qry = f"""SELECT GEOdata, county, case_count, income, population FROM gis 
                    JOIN census_data ON gis.county = census_data.id WHERE state = {state}"""

        cur.execute(qry)

        return cur.fetchall()

    def get_state_center(self, state):
        cur = self.db.get_cur()

        qry = f"SELECT latitude, longitude FROM gis_state_coordinates WHERE state = {state}"
        cur.execute(qry)

        return cur.fetchall()

    def get_max_ratio_state(self, state):
        cur = self.db.get_cur()

        qry = f"""SELECT MAX(case_count/population) as perc FROM gis JOIN census_data ON gis.county = census_data.id
                       WHERE gis.state = {state}"""
        cur.execute(qry)

        return cur.fetchall()

    def get_state_name(self, state):
        cur = self.db.get_cur()

        qry = f"SELECT meaning FROM state_code WHERE id = {state}"
        cur.execute(qry)

        return cur.fetchall()

    def get_state_offense_data(self, state):
        cur = self.db.get_cur()

        qry = f"""SELECT COUNT(*) as off_count, offense FROM (SELECT d2_code.meaning AS offense
                        FROM filing_data JOIN d2_code ON d2_code.id = filing_data.offense
                        WHERE filing_data.state = {state}) filing 
                        GROUP BY offense ORDER BY off_count desc"""

        cur.execute(qry)

        return cur.fetchall()

    def get_county_data(self, county):
        cur = self.db.get_cur()

        qry = f""" SELECT cases_data.id as id, defendant_key, proceeding_date, prison_time, prob_time, fine, 
                    d2_code.meaning as offense, disposition_code.meaning as disposition FROM 
                    (SELECT cases.id as id, defendant_key, proceeding_date, prison_time, prob_time, 
                    fine, offense, disposition FROM termination_data 
                    INNER JOIN (SELECT id, defendant_key, county, proceeding_date
                    FROM case_data WHERE county = {county}) cases ON termination_data.id = cases.id) cases_data 
                    JOIN d2_code ON cases_data.offense = d2_code.id 
                    JOIN disposition_code ON cases_data.disposition = disposition_code.id"""
        cur.execute(qry)

        return cur.fetchall()

    def get_county_name(self, county):
        cur = self.db.get_cur()

        qry = f"SELECT meaning FROM county_code WHERE id = {county}"
        cur.execute(qry)

        return cur.fetchall()
