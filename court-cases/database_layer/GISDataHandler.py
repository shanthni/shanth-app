import json
from database_layer.DatabaseUtils import DatabaseHandler


class GISDBHandler:
    def __init__(self, config):
        config = json.load(config)
        creds = config["MySQL"]
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], 'casedata')

    def create_gis_table(self, fields):
        attributes = {
            i: 'VARCHAR(50)' if i != 'GEOdata' else 'JSON' for i in fields
        }
        attributes['id'] = 'INT AUTO_INCREMENT PRIMARY KEY'

        self.db.create_table('GIS', attributes)

    def load_gis_data(self, fields, data):
        cur = self.db.get_cur()
        qry = 'INSERT INTO gis ({}) VALUES({})'.format(', '.join(fields),
                                                       ', '.join(['%s'] * (len(fields))))

        cur.executemany(qry, data)

        qry = f"CREATE INDEX gis_county_code ON gis (county_code)"
        cur.execute(qry)

        self.db.commit()

    def load_state_mapping(self, attributes, data):
        cur = self.db.get_cur()

        attributes = {
            code: 'VARCHAR (225)' for code in attributes
        }
        attributes['id'] = 'INT AUTO_INCREMENT NOT NULL PRIMARY KEY'
        self.db.create_table('state_code', attributes)

        qry = "INSERT INTO {} ({}) VALUES ({})".format('state_code',
                                                       ', '.join([i for i in attributes.keys() if i != 'id']),
                                                       ', '.join(['%s'] * (len(attributes) - 1)))

        cur.executemany(qry, data)
        self.db.commit()

    def update_county_ids(self):
        cur = self.db.get_cur()

        qry = f'ALTER TABLE gis ADD COLUMN county INT'
        cur.execute(qry)

        qry = f"""UPDATE gis INNER JOIN county_code ON gis.county_code = county_code.IDB_id SET 
                  county = county_code.id"""
        cur.execute(qry)

        qry = f'ALTER TABLE gis ADD COLUMN state INT'
        cur.execute(qry)

        qry = f"""UPDATE gis INNER JOIN state_code ON gis.state_code = state_code.IDB_id SET 
                          state = state_code.id"""
        cur.execute(qry)

        qry = f'ALTER TABLE gis DROP COLUMN state_code'
        cur.execute(qry)

        self.db.commit()
