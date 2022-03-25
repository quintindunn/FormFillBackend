from flask import Flask, request
from Parser import parse
import json


app = Flask(__name__)


@app.route("/post", methods=["POST"])
def post():
    try:
        data = request.data.decode()
        data = json.loads(data)
    except ValueError:
        return "400", 400
    print(json.dumps(data))
    return "200", 200


@app.route("/get", methods=["GET"])
def get():

    return "200", 200


app.run(host="0.0.0.0", port=84)
