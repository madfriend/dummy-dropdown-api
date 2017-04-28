import os
from functools import wraps
from flask import Flask, request, jsonify, current_app
from flask_cors import CORS
from flask_jsonpify import jsonify
import random
from test_data import data

app = Flask(__name__)
CORS(app)

@app.route("/search")
def search():
    return jsonify(random.sample(data, random.randint(1, 50)))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
