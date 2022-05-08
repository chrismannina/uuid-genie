from flask import *
import json

# import uuid generator
import app.uuid_generator as id

# create and initialize a new Flask app
app = Flask(__name__)

# root page
@app.route('/')
def root():
    return 'Use GET api/uuid/ to request a randomly generated UUID.'

# GET request - single uuid (version 4)
@app.route('/api/uuid/')
def uuid():
    """UUID generated and returned as JSON object."""
    data = {"uuid": f"{str(id.generate_uuid())}"}
    uuid = json.dumps(data)
    return uuid

# GET request - multiple uuids (version 4)
@app.route('/api/uuid/<number>')
def uuid_number(number):
    """Multiple UUIDs generated and returned as JSON object."""
    data_dict = {}
    for i in range(int(number)):
        data_dict[f"uuid-{i+1}"] = str(id.generate_uuid())
    uuids = json.dumps(data_dict)
    return uuids


if __name__ == '__main__':
    app.run(port=1337, debug=True)
