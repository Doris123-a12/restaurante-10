# Servicio encargado de administrar productos y usuarios.

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:

    def __init__(self) -> None:

        # Lista de productos del restaurante.
        self.productos: list[Producto] = []

        # Lista de usuarios del restaurante.
        self.usuarios: list[Usuario] = []
        
    # PRODUCTOS

    def registrar_producto(self, producto: Producto) -> bool:

        if self.buscar_producto(producto.codigo) is not None:
            return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:

        for producto in self.productos:

            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        return True

    def eliminar_producto(self, codigo: str) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        return True

    def listar_productos(self) -> None:

        if len(self.productos) == 0:
            print("\nNo existen productos registrados.")
            return

        print(" PRODUCTOS ")

        for producto in self.productos:
            producto.mostrar_informacion()

    def obtener_categorias(self) -> set[str]:

        categorias: set[str] = set()

        for producto in self.productos:
            categorias.add(producto.categoria)

        return categorias

    # USUARIOS

    def registrar_usuario(self, usuario: Usuario) -> bool:

        for usuario_registrado in self.usuarios:

            if usuario_registrado.identificacion == usuario.identificacion:
                return False

        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> None:

        if len(self.usuarios) == 0:
            print("No existen usuarios registrados.")
            return

        print(" USUARIOS ")

        for usuario in self.usuarios:
            usuario.mostrar_informacion()