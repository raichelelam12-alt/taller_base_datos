class Productos:
    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int):
        """Constructor de la clase Productos"""
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad: int):
        """Método para modificar el stock del producto"""
        self.stock += cantidad

    def obtener_detalles(self) -> str:
        """Método para retornar la información formateada del producto"""
        return f"ID: {self.id_producto} | Producto: {self.nombre} | Precio: ${self.precio:,.2f} | Stock: {self.stock} unidades"
