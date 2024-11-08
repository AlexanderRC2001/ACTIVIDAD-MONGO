import pymongo
import matplotlib.pyplot as plt

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Cambia la URL según tu configuración
db = client["actividad"]  # Nombre de la base de datos
collection = db["datos"]  # Nombre de la colección

# Filtrar datos por el indicador deseado (por ejemplo, "Incidencia del VIH")
indicador_deseado = "Incidencia del VIH"
cursor = collection.find({"Indicador": indicador_deseado}, {"_id": 0, "Entidad": 1, "Cantidad": 1})

# Procesar los datos para graficar
entidades = []
cantidades = []

for documento in cursor:
    entidades.append(documento["Entidad"])
    cantidades.append(documento["Cantidad"])

# Crear la gráfica
plt.figure(figsize=(12, 6))
plt.bar(entidades, cantidades, color="lightcoral")
plt.xlabel("Entidad")
plt.ylabel("Cantidad")
plt.title(f"{indicador_deseado} por Entidad")
plt.xticks(rotation=90)
plt.tight_layout()  # Ajusta el layout para que se vea bien
plt.show()
