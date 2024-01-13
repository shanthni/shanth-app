from database_layer.DatabaseUtils import DatabaseHandler
import json


class AppLogicDBHandler:
    def __init__(self, config):
        config = json.load(config)
        creds = config["MySQL"]
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], 'casedata')

    def get_county_data(self, state):
        cur = self.db.get_cur()

        qry = f"""SELECT * FROM gis WHERE state = {state}"""
        cur.execute(qry)

        return cur.fetchall()

