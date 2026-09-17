from flask import Flask, jsonify, request

app = Flask(__name__)

tareas = [
    {"id": 1, "titulo": "Aprender Docker", "hecha": False},
    {"id": 2, "titulo": "Crear una API con Flask", "hecha": True},
]


@app.route("/")
def inicio():
    return jsonify({"mensaje": "API funcionando correctamente"})


@app.route("/tareas", methods=["GET"])
def obtener_tareas():
    return jsonify(tareas)


@app.route("/tareas/<int:tarea_id>", methods=["GET"])
def obtener_tarea(tarea_id):
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(tarea)


@app.route("/tareas", methods=["POST"])
def crear_tarea():
    datos = request.get_json()
    nueva_tarea = {
        "id": len(tareas) + 1,
        "titulo": datos.get("titulo", ""),
        "hecha": False,
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
