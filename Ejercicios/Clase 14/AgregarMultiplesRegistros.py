# |-------------------------------------------|
# | Ejercicio 1 - Agregar multiples registros |
# |-------------------------------------------|

import sqlite3

# Me conecto a la base de datos (o la creo si no existe)
conexion = sqlite3.connect("personas.db")
cursor = conexion.cursor()

# Creo la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS Personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    ciudad TEXT NOT NULL
);
""")

# Lista de nuevas personas a agregar
nuevas_personas = [
    ("Esteban", 32, "Mar del Plata"),
    ("Valeria", 27, "Bahía Blanca"),
    ("Fernando", 41, "Rosario"),
    ("Carolina", 29, "La Plata"),
    ("Juan", 35, "Córdoba"),
    ("Sofía", 18, "Mendoza"),
    ("Lucas", 22, "Salta"),
    ("Martina", 30, "Bariloche"),
    ("Mateo", 19, "San Juan"),
    ("Julieta", 24, "Tucumán"),
    ("Tomás", 25, "Neuquén"),
    ("Camila", 20, "Santa Fe"),
    ("Ignacio", 26, "San Luis"),
    ("Florencia", 23, "Río Gallegos"),
    ("Agustina", 17, "Trelew"),
    ("Facundo", 21, "Jujuy"),
    ("Milagros", 16, "Ushuaia"),
    ("Ezequiel", 28, "Villa María"),
    ("Lara", 15, "Resistencia"),
    ("Santiago", 30, "Posadas")
]

# Agrego los registros en la tabla Personas
for persona in nuevas_personas:
    cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES (?, ?, ?)", persona)

# Acá se confirman los cambios
conexion.commit()

# Acá recupero y muestro todos los registros de la tabla Personas
cursor.execute("SELECT * FROM Personas")
registros = cursor.fetchall()

print("\nRegistros en la tabla Personas:")
for registro in registros:
    print(registro)

# Acá cierro la conexión 
conexion.close()
