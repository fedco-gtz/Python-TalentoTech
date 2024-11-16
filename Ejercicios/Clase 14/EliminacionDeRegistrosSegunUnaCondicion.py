# |------------------------------------------------------------|
# | Ejercicio 2 - Eliminación de registros según una condición |
# |------------------------------------------------------------|

import sqlite3

# Me conecto a la base de datos
conexion = sqlite3.connect("personas.db")
cursor = conexion.cursor()

# Elimino los registros donde la edad sea menor a 25
cursor.execute("DELETE FROM Personas WHERE edad < 25")

# Confirmo los cambios
conexion.commit()

# Recupero y muestro todos los registros restantes
cursor.execute("SELECT * FROM Personas")
registros = cursor.fetchall()

print("\nRegistros restantes en la tabla Personas:")
for registro in registros:
    print(registro)

# Acá cierro la conexión 
conexion.close()
