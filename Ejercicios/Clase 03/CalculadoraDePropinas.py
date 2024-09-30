# |---------------------------------------|
# | Ejercicio 2 - Calculadora de Propinas |
# |---------------------------------------|

# Se solicita el monto total de la cuenta al usuario
monto_total = float(input("Ingresa el monto total de la cuenta: "))

# Se solicita el porcentaje de propina al usuario
porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar (por ejemplo, 15 para 15%): "))

# Calculo de la propina
propina = (porcentaje_propina / 100) * monto_total

# Calcular el total a pagar (incluyendo la propina)
total_a_pagar = monto_total + propina

# Mostrar los resultados en pantalla
print(f"La cantidad de propina es: ${propina:.2f}")
print(f"El total a pagar, incluyendo la propina, es: ${total_a_pagar:.2f}")
