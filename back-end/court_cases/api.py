import json
import os
import logging
import traceback
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from court_cases.applogic_layer.court_cases_data import AppLogic

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

creds = os.getenv("CLEARDB_DATABASE_JSON")
creds = json.loads(creds)

data_API = AppLogic(creds)


@app.route('/state-data/<int:state>', methods=['GET'])
@cross_origin()
def state_data_api(state):
    try:
        return jsonify(data_API.state_level_data(state))
    except Exception as e:
        return logging.error(traceback.format_exc())


@app.route('/county-data/<int:county>', methods=['GET'])
@cross_origin()
def county_data_api(county):
    try:
        return jsonify(data_API.county_level_data(county))
    except Exception as e:
        return logging.error(traceback.format_exc())


if __name__ == '__main__':
    app.run(debug=True)
