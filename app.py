import json
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_get():
    return """
    <!DOCTYPE html>
    <head>
        <title>INDEX</title>
    </head>
    <body>
        <h1>Index</h1>
    </body>
    """

@app.route("/json", methods=["GET"])
def json_get():
    response = ''
    with open("example.json") as f:
        response = make_response(
            json.load(f),
            200
        )
    response.headers.add('Content-Type', 'application/json')
    return response

@app.route("/json", methods=["POST"])
def json_post():
    if request.json is not None:
        if request.json["title"] is not None and request.json["body"] is not None:
            the_json = {
                "title": request.json["title"],
                "body": request.json["body"]
            }
            with open("example.json", "w") as f:
                json.dump(the_json, f)
            return make_response(json.dumps({"JSON": "overwritten"}), 201)
        else:
            return make_response(json.dumps({"error": "JSON incorrectly formatted"}), 400)
    else:
        return make_response(json.dumps({"error": "JSON not included with request"}))


if __name__ == "__main__":
    app.run(port=7777)