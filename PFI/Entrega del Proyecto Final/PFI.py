import sqlite3
import os
import time

# Creación de base de datos y tablas si no existen
def inicializar_db():
    with sqlite3.connect("inventario.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        """)
        conn.commit()

def inicializar_db_usuarios():
    with sqlite3.connect("usuarios.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                contrasena TEXT NOT NULL
            )
        """)
        conn.commit()

# Función para agregar un nuevo producto
def registrar_producto():
    print("\n|-------------------------------------|")
    print("|    Registrando de nuevo producto    |")
    print("|-------------------------------------|")
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    with sqlite3.connect("inventario.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)""",
                       (nombre, descripcion, cantidad, precio, categoria)
                       )
        conn.commit()
    print("\nPRODUCTO REGISTRADO EXITOSAMENTE. 🎉\n")

# Función para mostrar todos los productos
def mostrar_productos():
    with sqlite3.connect("inventario.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

    if productos:
        print("\n|------------------|")
        print("|    Inventario    |")
        print("|------------------|")
        for producto in productos:
            print(f"ID: {producto[0]},\n    Nombre: {producto[1]},\n    Descripción: {producto[2]}"
                  f"\n    Cantidad: {producto[3]}\n    Precio: ${producto[4]:.2f}\n    Categoría: {producto[5]}\n")
    else:
        print("\nEL INVENTARIO ESTÁ VACÍO. 🛑\n")

# Función para actualizar el stock de un producto
def actualizar_producto():
    print("\n|--------------------------------------|")
    print("|    Actualizando stock de producto    |")
    print("|--------------------------------------|")
    id_producto = int(input("ID del producto a actualizar: "))
    nueva_cantidad = int(input("Nueva cantidad: "))

    with sqlite3.connect("inventario.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE productos
            SET cantidad = ?
            WHERE id = ?""", (nueva_cantidad, id_producto))
        conn.commit()

    if cursor.rowcount > 0:
        print("\nPRODUCTO ACTUALIZADO. ✅\n")
    else:
        print("\nNO SE ENCONTRÓ UN PRODUCTO CON ESE ID. 🔍\n")

# Función para eliminar un producto
def eliminar_producto():
    print("\n|---------------------------|")
    print("|    Eliminando producto    |")
    print("|---------------------------|")
    id_producto = int(input("ID del producto a eliminar: "))

    with sqlite3.connect("inventario.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conn.commit()

    if cursor.rowcount > 0:
        print("\nPRODUCTO ELIMINADO. 🗑️\n")
    else:
        print("\nNO SE ENCONTRÓ UN PRODUCTO CON ESE ID. ❌\n")

# Función para buscar productos
def buscar_producto():
    criterio = input("Buscar por (ID/NOMBRE/CATEGORIA): ").lower()
    valor = input("Valor de búsqueda: ")

    with sqlite3.connect("inventario.db") as conn:
        cursor = conn.cursor()
        if criterio == "id":
            cursor.execute("SELECT * FROM productos WHERE id = ?", (valor,))
        elif criterio == "nombre":
            cursor.execute(
                "SELECT * FROM productos WHERE nombre LIKE ?", (f"%{valor}%",))
        elif criterio == "categoria":
            cursor.execute(
                "SELECT * FROM productos WHERE categoria LIKE ?", (f"%{valor}%",))
        else:
            print("\nCRITERIO INVÁLIDO. ⚠️\n")
            return
        productos = cursor.fetchall()

    if productos:
        print("\n----- Resultados de búsqueda -----")
        for producto in productos:
            print(f"ID: {producto[0]}\n    Nombre: {producto[1]}\n    Descripción: {producto[2]}"
                  f"\n    Cantidad: {producto[3]}\n    Precio: ${producto[4]:.2f}\n    Categoría: {producto[5]}")
    else:
        print("\nNO SE ENCONTRARON PRODUCTOS QUE COINCIDAN CON LA BÚSQUEDA. 🔎\n")

# Función para generar un reporte de bajo stock
def reporte_bajo_stock():
    print("\n|-----------------------------|")
    print("|    Chequeando stock bajo    |")
    print("|-----------------------------|")
    limite = int(input("Especificar límite de stock: "))

    with sqlite3.connect("inventario.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        productos = cursor.fetchall()

    if productos:
        print("\n----- Productos con bajo stock -----")
        for producto in productos:
            print(
                f"ID: {producto[0]}\n    Nombre: {producto[1]}\n    Cantidad: {producto[3]}")
    else:
        print("\nNO HAY PRODUCTOS CON BAJO STOCK. 📦\n")

# Función para iniciar sesión
def iniciar_sesion():
    print("\n|------------------------|")
    print("|    Iniciando sesión    |")
    print("|------------------------|")
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    with sqlite3.connect("usuarios.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
        usuario_autenticado = cursor.fetchone()
    
    if usuario_autenticado:
        print(f"\n¡BIENVENIDO AL SISTEMA {usuario[:len(usuario)].upper()}! 🎉")
        return True
    else:
        print("\nUSUARIO O CONTRASEÑA INCORRECTOS. ❌")
        return False

# Función para registrar un nuevo usuario
def registrar_usuario():
    print("\n|---------------------------|")
    print("|    Registrando usuario    |")
    print("|---------------------------|")
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    with sqlite3.connect("usuarios.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuarios (usuario, contrasena)
                VALUES (?, ?)""", (usuario, contrasena))
            conn.commit()
            print("\nUSUARIO REGISTRADO EXITOSAMENTE. 🎉")
        except sqlite3.IntegrityError:
            print("\nEL NOMBRE DE USUARIO YA EXISTE. INTENTA CON OTRO. 🔄")

# Menú principal
def menu():
    while True:
        print("\n|----------------------|")
        print("|    Menú Principal    |")
        print("|----------------------|")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de bajo stock")
        print("7. Cerrar sesión")

        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("SALIENDO...\n¡HASTA LUEGO! 👋")
            time.sleep(2) 
            os.system('cls' if os.name == 'nt' else 'clear')
            inicio()
        else:
            print("OPCIÓN INVÁLIDA. ⚠️")

# Menú de inicio de sesión
def inicio():
    while True:
        print("\n|-------------------------|")
        print("|    Acesso al sistema    |")
        print("|-------------------------|")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            if iniciar_sesion():
                menu()  
                break
        elif opcion == "2":
          registrar_usuario()
        elif opcion == "3":
            print(f"SALIENDO...\n¡HASTA LUEGO! 👋")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear') 
            inicio()
        else:
            print("OPCIÓN INVÁLIDA. ⚠️")


# Iniciación de las bases de datos y ejecutar los menues
if __name__ == "__main__":
    inicializar_db()
    inicializar_db_usuarios()
    inicio()