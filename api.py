import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
f_lux = open('lux.json',)
f_humtem = open('humtem.json',)
f_solid = open('solid.json',)
data_lux= json.load(f_lux)
data_humtem= json.load(f_humtem)
data_solid= json.load(f_solid)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/lux', methods=['GET'])
def api_all():
    return jsonify(data_lux)
@app.route('/api/humtem', methods=['GET'])
def api_all():
    return jsonify(data_humtem)
    @app.route('/api/solid', methods=['GET'])
def api_all():
    return jsonify(data_solid)

app.run()