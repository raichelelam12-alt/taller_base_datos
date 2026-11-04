from producto import Productos
from cliente import Clientes

class Gestor_base_datos:
    def __init__(self):
        """Constructor del gestor de datos"""
        self.lista_productos = []
        self.lista_clientes = []

    def registrar_producto(self, producto: Productos):
        """Método para agregar un producto al sistema"""
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente: Clientes):
        """Método para agregar un cliente al sistema"""
        self.lista_clientes.append(cliente)

    def obtener_productos(self):
        """Método para retornar todos los productos"""
        return self.lista_productos

    def obtener_clientes(self):
        """Método para retornar todos los clientes"""
        return self.lista_clientes
