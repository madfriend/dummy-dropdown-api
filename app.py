import os
from flask import Flask, request, render_template, jsonify
import random
from test_data import data


app = Flask(__name__)

@app.route("/search")
def search():
    return jsonify(random.sample(data, random.randint(1, 50)))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
