from flask import Flask
from config import Configuration


app = Flask(__name__, static_folder=None)
app.config.from_object(Configuration())


@app.route("/greeting", methods=['GET'])
def hello():
    return "Hello World!"
