# |--------------------------------------|
# | Ejercicio 2 - Consumo de Combustible |
# |--------------------------------------|

# Función para calcular litros consumidos y dinero gastado
def calcular_consumo(cantidad_litros_100km, costo_por_litro, distancia_viaje):
    litros_consumidos = (cantidad_litros_100km / 100) * distancia_viaje
    dinero_gastado = litros_consumidos * costo_por_litro
    return litros_consumidos, dinero_gastado

# Solicitar los datos del usuario
litros_por_100km = float(input("Ingrese la cantidad de litros consumidos por cada 100 km: "))
costo_por_litro = float(input("Ingrese el costo por litro de combustible: "))
distancia_viaje = float(input("Ingrese la longitud del viaje (en kilómetros): "))

# Calcular litros consumidos y dinero gastado
litros_consumidos, dinero_gastado = calcular_consumo(litros_por_100km, costo_por_litro, distancia_viaje)

# Mostrar resultados
print("\n--- Detalle del Consumo ---")
print(f"Litros consumidos: {litros_consumidos:.2f} L")
print(f"Dinero gastado: ${dinero_gastado:.2f}")
