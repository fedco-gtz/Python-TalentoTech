Iniciación a la Programación con Python - Comisión 24217

- Profesor: FERNANDEZ, Jose
- Tutora Pedagógica (Desde 14/11): THEMTHAM, Natalia
- Estudiante: GUTIERREZ, Federico
________________________________________________________________________________________________________________________________________________
Descripción del Proyecto

Este es un sistema de gestión de inventario simple que permite registrar, actualizar, eliminar, buscar productos y generar reportes de bajo stock. Además, ofrece funcionalidades de gestión de usuarios, permitiendo tanto el registro como el inicio de sesión de usuarios para acceder a las opciones del sistema. El sistema utiliza bases de datos SQLite para almacenar tanto la información de los productos como los usuarios.
________________________________________________________________________________________________________________________________________________
Funcionalidades

1. Registrar producto
Permite registrar un nuevo producto en el inventario, ingresando detalles como nombre, descripción, cantidad, precio y categoría.

2. Mostrar productos
Muestra todos los productos almacenados en la base de datos del inventario, incluyendo su nombre, descripción, cantidad, precio y categoría.

3. Actualizar producto
Permite actualizar la cantidad disponible de un producto en el inventario, especificando el ID del producto y la nueva cantidad.

4. Eliminar producto
Elimina un producto del inventario usando su ID. Si el producto no existe, muestra un mensaje de error.

5. Buscar producto
Permite realizar búsquedas de productos por ID, nombre o categoría. Muestra los productos que coinciden con los criterios de búsqueda.

6. Reporte de bajo stock
Genera un reporte de productos con cantidad inferior a un límite especificado, útil para verificar qué productos necesitan ser reabastecidos.

7. Iniciar sesión
Los usuarios pueden iniciar sesión en el sistema proporcionando su nombre de usuario y contraseña. Si las credenciales son correctas, el usuario accede al sistema.

8. Registrar usuario
Permite registrar nuevos usuarios en el sistema con un nombre de usuario único y una contraseña. Si el nombre de usuario ya existe, muestra un mensaje de error.
________________________________________________________________________________________________________________________________________________
Herramientas Utilizadas

1. Python 3.x: Lenguaje de programación utilizado para desarrollar el sistema.
2. SQLite: Base de datos liviana usada para almacenar los datos de los productos y los usuarios.
3. os: Módulo para interactuar con el sistema operativo, usado para limpiar la pantalla de la terminal.
4. time: Módulo usado para pausar la ejecución del programa y crear una experiencia de usuario más fluida.
________________________________________________________________________________________________________________________________________________
Instrucciones para Ejecutar el Proyecto

1. Requisitos previos:
     - Tener instalado Python 3.x en tu PC.
     - Tener acceso a la terminal o línea de comandos.
2. Clonar el proyecto: Descarga todos los archivos de esta carpetaen tu PC.
3. Ejecutar el script: Abre la terminal en la carpeta donde se encuentra el archivo PFI.py y ejecuta el script (Posiblemente tengas que utilizar el comando "python PFI.py")
4. Interacción con el sistema:
     - El sistema mostrará un menú de inicio donde podrás iniciar sesión, registrarte o salir.
     - Si inicias sesión correctamente, accederás al menú principal donde podrás gestionar los productos del inventario.
________________________________________________________________________________________________________________________________________________
Notas Adicionales
1. Base de datos: Al ejecutar el código por primera vez, se crearán dos bases de datos: inventario.db para los productos y usuarios.db para los usuarios.
2. Seguridad: Este sistema no implementa cifrado de contraseñas, por lo que se recomienda utilizarlo únicamente en entornos controlados o de prueba.
3. Usuarios de Prueba:
     - Usuario: fedco                Contraseña: 1234
     - Usuario: tonif                Contraseña: 1234
     - Usuario: nataliath            Contraseña: 1234
________________________________________________________________________________________________________________________________________________
¡Gracias por utilizar este sistema de gestión de inventario! Si tienes alguna pregunta o sugerencia, no dudes en contactarme.