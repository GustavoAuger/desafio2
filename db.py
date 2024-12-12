from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Crear la conexión con MongoDB
def get_mongo_client():
    try:
        MONGO_URI = os.getenv("MONGO_URI")
        client = MongoClient(MONGO_URI)
        client.admin.command('ping')  # Prueba la conexión
        print("Conexión exitosa a MongoDB")
        return client
    except Exception as e:
        print("Error al conectar con MongoDB:", e)

# Obtener la base de datos y la colección
client = get_mongo_client()
db = client['mi_base_datos']
tareas_collection = db['tareas']


