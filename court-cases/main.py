from etl.CaseData import CDLoader

loader = CDLoader(open('../config.json'))
loader.do_load()
