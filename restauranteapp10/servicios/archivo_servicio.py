# Servicio encargado de guardar y cargar productos en formato JSON.

import json

from modelos.producto import Producto


class ArchivoServicio:

    def __init__(self, ruta_archivo: str) -> None:
        self.ruta_archivo: str = ruta_archivo

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> bool:

        datos_productos = []

        for producto in productos:
            datos_productos.append(producto.to_dict())

        try:

            with open(
                self.ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos_productos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except PermissionError:
            print(
                "Error: no existen permisos para "
                "escribir el archivo de productos."
            )
            return False

    def cargar_productos(self) -> list[Producto]:

        productos: list[Producto] = []

        try:

            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos_productos = json.load(archivo)

            for datos in datos_productos:

                try:

                    producto = Producto(
                        codigo=datos["codigo"],
                        nombre=datos["nombre"],
                        categoria=datos["categoria"],
                        precio=float(datos["precio"])
                    )

                    productos.append(producto)

                except KeyError as error:

                    print(
                        f"Advertencia: falta la clave "
                        f"{error} en un producto del archivo."
                    )

                except ValueError as error:

                    print(
                        f"Advertencia: producto inválido "
                        f"en el archivo: {error}"
                    )

            return productos

        except FileNotFoundError:

            print(
                "No existe el archivo de productos."
                "Se iniciará el sistema con una colección vacía."
            )

            return []

        except json.JSONDecodeError:

            print(
                "Error: el archivo productos.json "
                "no contiene un formato JSON válido."
            )

            return []

        except PermissionError:

            print(
                "Error: no existen permisos para "
                "leer el archivo de productos."
            )

            return []