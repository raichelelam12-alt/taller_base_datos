class Clientes:
    def __init__(self, cedula: str, nombre: str, correo: str):
        """Constructor de la clase Clientes"""
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo

    def obtener_detalles(self) -> str:
        """Método para retornar la información formateada del cliente"""
        return f"Cédula: {self.cedula} | Nombre: {self.nombre} | Correo: {self.correo}"
