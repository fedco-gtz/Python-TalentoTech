# |----------------------------------------------|
# | Ejercicio 1 - Conceptualización de una tabla |
# |----------------------------------------------|

# 1) Nombre de la tabla: biblioteca_escolar

# 2) Campos de la tabla: id_libro (INT, PRIMARY KEY, AUTO_INCREMENT), 
#                        titulo (VARCHAR(255), NOT NULL)
#                        autor (VARCHAR(255), NOT NULL)
#                        fecha_publicacion (DATE, NULLABLE)
#                        genero (VARCHAR(100), NOT NULL)
#                        cantidad_ejemplares (INT, DEFAULT 1)

# 3) Esquema en SQL
# |---------------------------------------------|
# |CREATE TABLE biblioteca_escolar (            |
# |    id_libro INT AUTO_INCREMENT PRIMARY KEY, |
# |    titulo VARCHAR(255) NOT NULL,            |
# |    autor VARCHAR(255) NOT NULL,             |
# |    fecha_publicacion DATE NULL,             |
# |    genero VARCHAR(100) NOT NULL,            |
# |    cantidad_ejemplares INT DEFAULT 1        |
# |);                                           |
# |---------------------------------------------|