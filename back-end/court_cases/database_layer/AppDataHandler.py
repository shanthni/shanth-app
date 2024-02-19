from Utils.DatabaseUtils import DatabaseHandler


class AppLogicDBHandler:
    def __init__(self, creds):
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], creds['db'])

    def get_geo_data(self, state):
        qry = f"""SELECT GEOdata, gis.county AS county, case_count, income, 
                    population, (case_count/population) as case_ratio FROM gis 
                    JOIN census_data ON gis.county = census_data.county WHERE gis.state = {state}"""

        self.db.execute(qry)

        return self.db.fetchall()

    def get_state_center(self, state):
        qry = f"SELECT latitude, longitude FROM gis_state_coordinates WHERE state = {state}"
        self.db.execute(qry)

        return self.db.fetchall()

    def get_state_name(self, state):
        qry = f"SELECT meaning FROM state_code WHERE id = {state}"
        self.db.execute(qry)

        return self.db.fetchall()

    def get_state_offense_data(self, state):
        qry = f"""SELECT off_count, d2_code.meaning as offense FROM 
                    (SELECT COUNT(*) as off_count, offense FROM filing_data 
                    WHERE state = {state} GROUP BY offense ORDER BY off_count desc LIMIT 10) filing 
                    JOIN d2_code ON d2_code.id = filing.offense"""

        self.db.execute(qry)

        return self.db.fetchall()

    def get_state_stats(self, state):
        qry = f"""SELECT AVG(prob_time) as stat, 'probation' as title 
                    FROM termination_data WHERE state = {state} and prob_time > 0
                    UNION SELECT AVG(prison_time) as stat, 'prison' as title 
                    FROM termination_data WHERE state = {state} and prison_time > 0
                    UNION SELECT AVG(fine) as stat, 'fine' as title 
                    FROM termination_data WHERE state = {state} and fine > 0
                    UNION SELECT SUM(case_count) as stat, 'case_count' as title 
                    FROM gis WHERE state = {state}"""

        self.db.execute(qry)

        return self.db.fetchall()

    def get_county_data(self, county):
        qry = f""" SELECT termination_data.id, defendant_key, proceeding_date, prison_time, prob_time, fine, 
                        d2_code.meaning AS offense, disposition_code.meaning As disposition FROM termination_data
                        JOIN case_data ON termination_data.case_id = case_data.case_id
                        JOIN d2_code ON termination_data.offense = d2_code.id
                        JOIN disposition_code ON termination_data.disposition = disposition_code.id
                        WHERE termination_data.county = {county}"""
        self.db.execute(qry)

        return self.db.fetchall()

    def get_county_name(self, county):
        qry = f"SELECT meaning FROM county_code WHERE id = {county}"
        self.db.execute(qry)

        return self.db.fetchall()

    def close_connection(self):
        self.db.close_connection()

    def open_connection(self):
        self.db.connect_to_db()
