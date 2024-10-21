# |-------------------------------------------------|
# | Desafio 1 - Datos personales en formato tarjeta |
# |-------------------------------------------------|

from datetime import datetime

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
ciudad = input("Ingresa tu ciudad de residencia: ")

anio_actual = datetime.now().year
edad = anio_actual - anio_nacimiento

nombre_completo = f"{apellido.upper()}, {nombre.capitalize()}"

correo_electronico = f"{nombre[0].lower()}.{apellido.lower()}{anio_nacimiento}@empresa.com.ar"

ciudad_mayus = ciudad.upper()

print("="*40)
print(f"Nombre completo: {nombre_completo}")
print(f"Año de nacimiento: {anio_nacimiento}")
print(f"Correo electrónico: {correo_electronico}")
print(f"Ciudad de residencia: {ciudad_mayus}")
print(f"Edad aproximada: {edad} años")
print("="*40)
