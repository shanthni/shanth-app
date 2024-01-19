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

    def create_coordinate_table(self, fields):
        attributes = {
            i: "DOUBLE" if i != 'state_name' else 'VARCHAR(50)' for i in fields
        }

        self.db.create_table('gis_state_coordinates', attributes)

    def load_coordinate_data(self, fields, data):

        cur = self.db.get_cur()

        qry = f'INSERT INTO gis_state_coordinates ({", ".join(fields)}) VALUES (%s, %s, %s)'

        cur.executemany(qry, data)

    def load_gis_data(self, fields, data):
        cur = self.db.get_cur()
        qry = 'INSERT INTO gis ({}) VALUES({})'.format(', '.join(fields),
                                                       ', '.join(['%s'] * (len(fields))))

        cur.executemany(qry, data)

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

    def update_gis_ids(self):
        cur = self.db.get_cur()

        qry = 'ALTER TABLE gis ADD COLUMN county INT'
        cur.execute(qry)

        qry = """UPDATE gis INNER JOIN county_code ON gis.county_code = county_code.IDB_id SET 
                  county = county_code.id"""
        cur.execute(qry)

        qry = 'ALTER TABLE gis ADD COLUMN state INT'
        cur.execute(qry)

        qry = """UPDATE gis INNER JOIN state_code ON gis.state_code = state_code.IDB_id SET 
                          state = state_code.id"""
        cur.execute(qry)

        qry = 'ALTER TABLE gis DROP COLUMN state_code'
        cur.execute(qry)

        qry = 'ALTER TABLE gis DROP COLUMN county_code'
        cur.execute(qry)

        self.db.commit()

    def get_case_counts(self):
        cur = self.db.get_cur()

        qry = 'ALTER TABLE gis ADD COLUMN case_count INT'
        cur.execute(qry)

        qry = """UPDATE gis JOIN (SELECT a.gis_id, COUNT(*) as case_count FROM (SELECT gis.id as gis_id 
                FROM case_data JOIN gis ON case_data.county = gis.county) a GROUP BY a.gis_id) counts ON 
                counts.gis_id = gis.id SET gis.case_count = counts.case_count"""
        cur.execute(qry)

        self.db.commit()

    def update_coordinate_ids(self):
        cur = self.db.get_cur()

        qry = f'ALTER TABLE gis_state_coordinates ADD COLUMN state INT'
        cur.execute(qry)

        qry = """UPDATE gis_state_coordinates INNER JOIN state_code ON 
                        gis_state_coordinates.state_name = state_code.meaning SET state = state_code.id"""
        cur.execute(qry)

        qry = f'ALTER TABLE gis_state_coordinates DROP COLUMN state_name'
        cur.execute(qry)

        self.db.commit()

