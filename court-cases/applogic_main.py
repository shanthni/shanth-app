from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from applogic_layer.court_cases_data import AppLogic

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
county_API = AppLogic(open('../config.json'))


@app.route('/state-data/<int:state>', methods=['GET'])
@cross_origin()
def state_data_api(state):
    return jsonify(county_API.state_level_data(state))


@app.route('/county-data/<int:county>', methods=['GET'])
@cross_origin()
def county_data_api(county):
    return jsonify(county_API.county_level_data(county))


if __name__ == '__main__':
    app.run(debug=True)
