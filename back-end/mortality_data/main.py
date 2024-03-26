import json

from mortality_data.etl.MortalityData import MortalityDataLoader

config = open('../config.json')
config = json.load(config)
config = config['MySQL']

mortality_loader = MortalityDataLoader(config)
mortality_loader.do_load()
