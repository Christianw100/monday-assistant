from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensaje": "¡Tu API está corriendo!"})

@app.route("/ping")
def ping():
    return jsonify({"status": "ok"})

@app.route("/listar-pendientes")
def listar_pendientes():
    board_id = TU_BOARD_ID_AQUI  # ← REEMPLAZA con tu verdadero board ID
    status_col_id = "status"

    query = """
    query ($board: [Int]) {
      boards(ids: $board) {
        items {
          id
          name
          column_values(ids: ["%s"]) {
            text
          }
        }
      }
    }
    """ % status_col_id

    variables = {"board": board_id}
    headers = {
        "Authorization": os.environ["MONDAY_API_KEY"]
    }

    response = requests.post(
        "https://api.monday.com/v2",
        json={"query": query, "variables": variables},
        headers=headers
    )

    if response.status_code != 200:
        return jsonify({"error": "No se pudo consultar Monday"}), 500

    data = response.json()
    try:
        items = data["data"]["boards"][0]["items"]
        pendientes = [
            {"id": item["id"], "nombre": item["name"]}
            for item in items
            if item["column_values"][0]["text"] != "Done"
        ]
        return jsonify({"pendientes": pendientes})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

