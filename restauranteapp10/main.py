# Archivo principal del sistema de restaurante.

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio



restaurante = Restaurante()

archivo_servicio = ArchivoServicio(
    "datos/productos.json"
)

# Cargar productos guardados anteriormente

productos_guardados = archivo_servicio.cargar_productos()

for producto in productos_guardados:
    restaurante.registrar_producto(producto)

# FUNCIONES DEL MENÚ

def registrar_producto() -> None:

    print("REGISTRAR PRODUCTO")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()

    try:

        precio = float(input("Precio: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        if restaurante.registrar_producto(producto):

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print("Producto registrado correctamente.")

        else:

            print(
                "Ya existe un producto con ese código."
            )

    except ValueError as error:

        print(f"Error: {error}")


def buscar_producto() -> None:

    print(" BUSCAR PRODUCTO")

    codigo = input(
        "Ingrese el código del producto: "
    ).strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is not None:
        producto.mostrar_informacion()

    else:
        print("Producto no encontrado.")


def actualizar_producto() -> None:

    print(" ACTUALIZAR PRODUCTO ")

    codigo = input(
        "Ingrese el código del producto: "
    ).strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:

        print("Producto no encontrado.")
        return

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    try:

        precio = float(input("Nuevo precio: ")
        )

        restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        archivo_servicio.guardar_productos(
            restaurante.productos
        )

        print(
            "Producto actualizado correctamente."
        )

    except ValueError as error:

        print(f"Error: {error}")


def eliminar_producto() -> None:

    print(" ELIMINAR PRODUCTO ")

    codigo = input(
        "Ingrese el código del producto: "
    ).strip()

    eliminado = restaurante.eliminar_producto(codigo)

    if eliminado:

        archivo_servicio.guardar_productos(
            restaurante.productos
        )

        print(
            "Producto eliminado correctamente."
        )

    else:

        print("Producto no encontrado.")
def listar_productos() -> None:

    restaurante.listar_productos()


def registrar_usuario() -> None:

    print("REGISTRAR USUARIO")

    identificacion = input(
        "Identificación: "
    ).strip()

    nombre = input(
        "Nombre: "
    ).strip()

    correo = input(
        "Correo: "
    ).strip()

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_usuario(usuario):

        print(
            "Usuario registrado correctamente."
        )

    else:

        print(
            "Ya existe el usuario"
        )

def listar_usuarios() -> None:

    restaurante.listar_usuarios()

def mostrar_categorias() -> None:

    print(" CATEGORÍAS ")

    categorias = restaurante.obtener_categorias()

    if len(categorias) == 0:

        print(
            "No existen categorías registradas."
        )

        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")

opciones_menu = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Salir"
)
# Diccionario 
acciones_menu = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": listar_usuarios,
    "8": mostrar_categorias
}

# MENÚ PRINCIPAL

while True:

    print("        SISTEMA DE RESTAURANTE")

    for numero, opcion_menu in enumerate(
        opciones_menu,
        start=1
    ):

        if numero == 6 or numero == 9:
            print("----------------------------------------")

        print(f"{numero}. {opcion_menu}")

    opcion = input(
        "Seleccione una opción: "
    ).strip()

    if opcion == "9":

        print(
            "Gracias por utilizar "
            "el sistema de restaurante."
        )

        break

    accion = acciones_menu.get(opcion)

    if accion is not None:

        accion()

    else:

        print("Opción no válida.")