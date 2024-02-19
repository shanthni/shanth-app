from Utils.DatabaseUtils import DatabaseHandler


class CensusDBHandler:
    def __init__(self, creds):
        self.db = DatabaseHandler(creds['host'], creds['user'], creds['password'], creds['db'])

    def load_census_data(self, table_name, data, fields):
        attributes = {
            i: "INT" if i != 'county' else 'VARCHAR(50)' for i in fields
        }
        attributes['id'] = 'INT AUTO_INCREMENT PRIMARY KEY'

        self.db.create_table(table_name, attributes)

        self.db.bulk_insert(table_name, fields, data)

        print(f'Loaded {table_name} data\n')

    def merge_tables(self):
        cur = self.db.get_cur()

        qry = """CREATE TABLE census_data AS	
                 SELECT county_code.id AS county, population, income FROM county_code 
                 JOIN census_population ON county_code.IDB_id = census_population.county
                 JOIN census_income ON county_code.IDB_id = census_income.county"""

        cur.execute(qry)

        self.db.commit()

        qry = "ALTER TABLE census_data ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
        cur.execute(qry)

        self.db.commit()

        qry = "DROP TABLE census_income"
        cur.execute(qry)

        qry = "DROP TABLE census_population"
        cur.execute(qry)

        self.db.commit()


