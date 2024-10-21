# |-----------------------------------------------|
# | Ejercicio 5 - Menú de opciones (más avanzado) |
# |                                               |
# | Crear un menú simple con 3 opciones.          |
# | El programa debe permitir al usuario elegir   |
# | entre sumar números, contar números pares e   |
# | impares, o salir del programa. El bucle debe  |
# | continuar hasta que el usuario elija la       |
# | opción de salir.                              |
# |-----------------------------------------------|

def sumar_numeros():
    cantidad = int(input("¿Cuántos números desea sumar? "))
    suma_total = 0
    for i in range(cantidad):
        numero = float(input(f"Ingrese el número {i+1}: "))
        suma_total += numero
    print(f"La suma total es: {suma_total}")

def contar_pares_impares():
    cantidad = int(input("¿Cuántos números desea ingresar? "))
    pares = 0
    impares = 0
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i+1}: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")

while True:
    print("\n--- Menú de Opciones ---")
    print("1. Sumar números")
    print("2. Contar números pares e impares")
    print("3. Salir")
    
    opcion = input("Elija una opción (1/2/3): ")
    
    if opcion == '1':
        sumar_numeros()
    elif opcion == '2':
        contar_pares_impares()
    elif opcion == '3':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
