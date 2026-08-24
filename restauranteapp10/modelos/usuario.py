 #Clase que representa a un usuario del restaurante.


class Usuario:

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:

        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> None:
        print("\n----- Usuario -----")
        print(f"Identificación: {self.identificacion}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")