import os
import operator

from flask import Flask, request
from flask_cors import CORS
from flask_jsonpify import jsonify

from test_data import data


app = Flask(__name__)
CORS(app)


@app.route("/search")
def search():
    prefixes = request.args.getlist('query')

    lst = []
    for (name, domain) in data:
        if len(prefixes) == 0 or any((domain.startswith(pr) for pr in prefixes)):
            lst.append(name)

    return jsonify(lst)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
