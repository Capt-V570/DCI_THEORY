from flask import Flask, jsonify


app = Flask(__name__) # class

@app.route("/")
def hello_world():
    return jsonify({"greeting": "Wir sind coole Leute"})