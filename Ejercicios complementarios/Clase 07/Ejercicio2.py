# |-------------------------------------------------------|
# | Ejercicio 2 - Contar productos con precio mayor a 100 |
# |                                                       |
# | Dada una lista de precios de productos, escribe un    |
# | programa que cuente cuántos productos tienen un       |
# | mayor a 100.                                          |
# | Lista de precios de productos                         |
# | precios = [150, 80, 120, 55, 200, 90]                 |
# |-------------------------------------------------------|

precios = [150, 80, 120, 55, 200, 90]

contador = sum(1 for precio in precios if precio > 100)

print("La cantidad de productos con precio mayor a 100 es:", contador)
