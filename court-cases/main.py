from etl.CaseData import CDLoader
from etl.GISData import GISDataLoader
from etl.CensusData import CensusDataLoader

case_loader = CDLoader(open('../config.json'))
case_loader.do_load()

gis_loader = GISDataLoader(open('../config.json'))
gis_loader.do_load()

census_loader = CensusDataLoader(open('../config.json'))
census_loader.do_load()

