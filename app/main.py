from flask import *
import json

# import uuid generator
import app.uuid_generator as id

# create and initialize a new Flask app
app = Flask(__name__)

# root page
@app.route('/', methods=['GET'])
def root():
    return 'Use GET /uuid to request a randomly generated UUID.'

# GET request
@app.route('/uuid/', methods=['GET'])
def request_page():
    """UUID generated and returned as JSON object."""
    uuid = id.generate_uuid()
    data_set = {'UUID': f'{uuid}'}
    json_uuid = json.dumps(data_set)
    return json_uuid


if __name__ == '__main__':
    app.run(port=1337, debug=True)
