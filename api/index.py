import os
import requests

@app.route("/listar-pendientes")
def listar_pendientes():
    board_id = TU_BOARD_ID_AQUI  # ← reemplázalo con el ID real de tu tablero
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

    data = response.json()
    items = data["data"]["boards"][0]["items"]

    pendientes = [
        {"id": item["id"], "nombre": item["name"]}
        for item in items
        if item["column_values"][0]["text"] != "Done"
    ]

    return jsonify({"pendientes": pendientes})
