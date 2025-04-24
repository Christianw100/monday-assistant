from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensaje": "¡Tu API está corriendo!"})

@app.route("/ping")
def ping():
    return jsonify({"status": "ok"})

@app.route("/get-token")
def get_token():
    clave_usuario = request.args.get("clave")
    CLAVE_CORRECTA = "mondaygpt123"  # Cambia esta clave si quieres

    if clave_usuario != CLAVE_CORRECTA:
        return jsonify({"error": "No autorizado"}), 401

    return jsonify({"token": os.environ["MONDAY_API_KEY"]})
