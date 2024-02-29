import json
import os

from court_cases.etl.CaseData import CDLoader
from court_cases.etl.GISData import GISDataLoader
from court_cases.etl.CensusData import CensusDataLoader

config = os.getenv("CLEARDB_DATABASE_JSON")
config = json.loads(config)

case_loader = CDLoader(config)
case_loader.do_load()

gis_loader = GISDataLoader(config)
gis_loader.do_load()

census_loader = CensusDataLoader(config)
census_loader.do_load()

