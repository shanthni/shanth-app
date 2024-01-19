from etl.CaseData import CDLoader
from etl.GISData import GISDataLoader

case_loader = CDLoader(open('../config.json'))
# case_loader.do_load()

gis_loader = GISDataLoader(open('../config.json'))
gis_loader.do_load()

