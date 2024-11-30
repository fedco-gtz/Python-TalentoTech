# |-------------------------------------------------------------|
# | Ejercicio 5 -  Diseña un progrma que implemente una         |
# | calculadora modular siguiendo las siguientes instrucciones: |
# | Crea una función menu_calculadora que haga lo siguiente:    |
# | 1. Solicite al usuario ingresar dos números.                |
# | 2. Muestre un menú con las siguientes opciones:             |
# |    a. Sumar dos números.                                    |
# |    b. Restar dos números.                                   |
# |    c. Dividir dos números.                                  |
# |    d. Multiplicar dos números.                              |
# |    e. Salir de la calculadora.                              |
# | 3. Según la opción seleccionada, llame a otra funcion que   |
# | realice el cálculo correspondiente.                         |
# | 4. Crea funciones independientes para realizar las          |
# | operaciones matemáticas (por ejemplo, sumar, restar, etc.), |
# | las cuales deben:                                           |
# |    a. Recibir los números como parámetros.                  |
# |    b. Realizar el cálculo y mostrar el resultado.           |
# |    c. Solicitar al usuario presionar 'Enter' para regresar  | 
# |       al menú principal.                                    |
# | 5. El programa debe repetirse hasta que el usuario          |
# | selecciones la opción 'Salir'.                              |
# |-------------------------------------------------------------|

def sumar(a, b):
    print(f"La suma de {a} y {b} es: {a + b}")
    input("Presiona 'Enter' para volver al menú principal...")

def restar(a, b):
    print(f"La resta de {a} y {b} es: {a - b}")
    input("Presiona 'Enter' para volver al menú principal...")

def dividir(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"La división de {a} entre {b} es: {a / b}")
    input("Presiona 'Enter' para volver al menú principal...")

def multiplicar(a, b):
    print(f"La multiplicación de {a} por {b} es: {a * b}")
    input("Presiona 'Enter' para volver al menú principal...")

def menu_calculadora():
    while True:
        print("\nCalculadora Modular")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Dividir dos números")
        print("4. Multiplicar dos números")
        print("5. Salir de la calculadora")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Por favor, ingresa valores numéricos.")
                continue

            if opcion == "1":
                sumar(num1, num2)
            elif opcion == "2":
                restar(num1, num2)
            elif opcion == "3":
                dividir(num1, num2)
            elif opcion == "4":
                multiplicar(num1, num2)
        elif opcion == "5":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

menu_calculadora()
