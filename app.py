from flask import Flask, request, jsonify, url_for
from config import Configuration
from model import db, ma


app = Flask(__name__, static_folder=None)
app.config.from_object(Configuration())

db.init_app(app)
ma.init_app(app)


# Route Creation
@app.route("/greeting", methods=['GET'])
def hello():
    return "Hello World!"


# Parameterized Route
@app.route("/greeting/<int:id>", methods=['GET'])
def hello_id(id):
    return "Hello World!" + str(id)


# Access Query String
@app.route("/greeting/bad", methods=['GET'])
def bad_greeting():
    exclamation = request.args.get('exclamation', 0)
    try:
        exclamation = int(exclamation)
    except TypeError:
        exclamation = 0
    greeting = "Hello World"
    for _ in range(exclamation):
        greeting += "!"

    return greeting


# Access JSON Payload
@app.route("/greeting/bad", methods=['POST'])
def post_bad_greeting():
    payload = request.get_json()
    exclamation = payload.get('exclamation', 0)
    try:
        exclamation = int(exclamation)
    except TypeError:
        exclamation = 0
    greeting = "Hello World"
    for _ in range(exclamation):
        greeting += "!"

    return greeting


# Return Status Code
@app.route("/not_found", methods=['GET'])
def not_found():
    return "not found", 404


# Return HTTP Header
@app.route("/location", methods=['GET'])
def locations():
    return "locations", 200, {"Location": url_for("locations")}


# Return JSON
# Access pass urls
@app.route("/routes", methods=['GET'])
def routes():
    jdict = {
        'greeting': url_for('hello', _external=True),
        'greeting_1': url_for('hello_id', id=1),
        'bad_greeting': url_for('bad_greeting'),
        'post_bad_greeting': url_for('post_bad_greeting'),
        'not_found': url_for('not_found'),
        'locations': url_for('locations'),
        'routes': url_for('routes'),
    }
    return jsonify(jdict)