import json

from court_cases.etl.CaseData import CDLoader
from court_cases.etl.GISData import GISDataLoader
from court_cases.etl.CensusData import CensusDataLoader

config = open('config.json')
config = json.load(config)
config = config["remote"]

case_loader = CDLoader(config)
case_loader.do_load()

gis_loader = GISDataLoader(config)
gis_loader.do_load()

census_loader = CensusDataLoader(config)
census_loader.do_load()

