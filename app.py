from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"mensaje": "¡Tu API está corriendo!"})

@app.route("/ping")
def ping():
    return jsonify({"status": "ok"})
