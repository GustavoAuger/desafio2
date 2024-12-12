from flask import Flask, jsonify, request
from db import tareas_collection
from models import TaskSchema


app = Flask(__name__)

# Crear instancia del esquema de validación
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


# Listar tareas
@app.route("/listar_tareas", methods=["GET"])
def listar_tareas():
    try:
        # Buscar todas las tareas
        tareas = list(tareas_collection.find())
        for tarea in tareas:
            del tarea["_id"]  # Eliminar el campo '_id' para enviar solo datos útiles
        return jsonify(tareas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Crear una tarea
@app.route("/crear_tarea", methods=["POST"])
def crear_tarea():
    try:
        # Validar datos con Marshmallow
        data = request.get_json()
        validated_data = task_schema.load(data)  # Validar datos

        # Insertar en la base de datos
        tareas_collection.insert_one(validated_data)
        return jsonify({"message": "Tarea creada"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
