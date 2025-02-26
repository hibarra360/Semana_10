import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:
    def __init__(self):
        # Se utiliza un diccionario para almacenar los productos con el ID como clave
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()

    def buscar_producto(self, nombre):
        return [p.to_dict() for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_todos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivo(self):
        # Se almacena el inventario en un archivo JSON para persistencia
        with open("inventario.json", "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f)

    def cargar_desde_archivo(self):
        try:
            # Se carga el inventario desde un archivo JSON si existe
            with open("inventario.json", "r") as f:
                datos = json.load(f)
                for item in datos:
                    self.productos[item["id_producto"]] = Producto(
                        item["id_producto"], item["nombre"], item["cantidad"], item["precio"]
                    )
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}


def menu():
    inventario = Inventario()
    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto: ")
            resultados = inventario.buscar_producto(nombre)
            print(resultados if resultados else "Producto no encontrado.")
        elif opcion == "5":
            print(inventario.mostrar_todos())
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
