from producto import Productos
from cliente import Clientes
from database import Gestor_base_datos

def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE GESTIÓN - UFPS         ")
    print("========================================")
    print("1. Registrar Producto")
    print("2. Registrar Cliente")
    print("3. Visualizar Productos")
    print("4. Visualizar Clientes")
    print("5. Salir")
    print("========================================")

def ejecutar_sistema():
    db = Gestor_base_datos()

    # Datos de prueba iniciales para visualización inmediata en consola
    db.registrar_producto(Productos(1, "Laptop Gamer", 3500000.0, 5))
    db.registrar_cliente(Clientes("1090123456", "Ana Pérez", "ana.perez@email.com"))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Registro de Nuevo Producto ---")
            try:
                id_prod = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese nombre del producto: ")
                precio = float(input("Ingrese precio: "))
                stock = int(input("Ingrese stock inicial: "))
                
                nuevo_prod = Productos(id_prod, nombre, precio, stock)
                db.registrar_producto(nuevo_prod)
                print("¡Producto registrado con éxito!")
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos.")

        elif opcion == "2":
            print("\n--- Registro de Nuevo Cliente ---")
            cedula = input("Ingrese cédula del cliente: ")
            nombre = input("Ingrese nombre completo: ")
            correo = input("Ingrese correo electrónico: ")
            
            nuevo_cliente = Clientes(cedula, nombre, correo)
            db.registrar_cliente(nuevo_cliente)
            print("¡Cliente registrado con éxito!")

        elif opcion == "3":
            print("\n--- VISUALIZACIÓN DE PRODUCTOS ---")
            productos = db.obtener_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                for p in productos:
                    print(f"-> {p.obtener_detalles()}")

        elif opcion == "4":
            print("\n--- VISUALIZACIÓN DE CLIENTES ---")
            clientes = db.obtener_clientes()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for c in clientes:
                    print(f"-> {c.obtener_detalles()}")

        elif opcion == "5":
            print("\nSaliendo del sistema... ¡Éxitos con tu entrega en GitHub!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    ejecutar_sistema()
