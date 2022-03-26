from flask import Flask, request

import Parser
import importlib
import json


app = Flask(__name__)


@app.route("/postFiller", methods=["POST"])
def postFiller():
    try:
        data = request.data.decode()
        data = json.loads(data)
    except ValueError:
        return "400", 400
    print(data)
    return "200", 200


@app.route("/postMail", methods=["POST"])
def postMail():
    importlib.reload(Parser)
    try:
        data = request.data
        Parser.parse(data)
    except ValueError:
        return "400", 400
    return "200", 200



@app.route("/get", methods=["GET"])
def get():

    return "200", 200


app.run(host="0.0.0.0", port=84)
