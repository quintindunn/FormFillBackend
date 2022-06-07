from flask import Flask, request

import Parser
import importlib
import json
import os
import time
import urllib.parse


app = Flask(__name__)


@app.route("/postFiller", methods=["POST"])
def postFiller():
    try:
        data = request.data.decode()
        body = json.loads(data)
    except ValueError:
        return "400", 400
    identifier = body[1]['identifier']
    data = body[0]["requestBody"]["formData"]
    base_url = body[0]['url'].replace("formResponse", "viewform")
    url = base_url + "?usp=pp_fill"
    if 'pageHistory' in data.keys():
        for i in data:
            if i.endswith("_sentinel") or not i.startswith("entry."):
                continue
            for x in data[i]:
                url += f"&{urllib.parse.quote(i)}={urllib.parse.quote(x)}"
        for i in "":
            if i.lower() in url.lower():
                name = i
                break

        print(url)
        print(body[-1])
    return url, 200


@app.route("/postMail", methods=["POST"])
def postMail():
    importlib.reload(Parser)
    try:

        data = request.data
        submission_count = int(json.loads(request.headers['sub_count'])['sub_count']) - 1

        identifier = json.loads(request.headers['Identifier'])['identifier']
        results = Parser.parse(data)
        results['identifier'] = identifier
        if not os.path.isdir(f"./{identifier}"):
            os.mkdir(f"./{identifier}")
        with open(f"./{identifier}/{submission_count}._.{results['form'].replace(' ', '_')}._.{time.time_ns()}.json", 'w') as f:
            json.dump(results, f, indent=2)
        # print(results)
    except ValueError:
        return "400", 200
    return "200", 200


@app.route("/get", methods=["GET"])
def get():

    return "200", 200


app.run(host="0.0.0.0", port=84)











# ['Abby', 'Zeke', 'Lily', 'Lily', 'Marcus', 'Lucy', 'Jordan', 'David', 'Nick', 'Drew', 'Lukas',
#                   'Ginger', 'Kali', 'Graelyn', 'Kaitlyn', 'Zoe', 'Gavin', 'Alessandro', 'Quintin', "Nicolas"]