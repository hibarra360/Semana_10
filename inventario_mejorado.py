import os

INVENTARIO_FILE = "inventario.txt"

def cargar_inventario():
    inventario = {}
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    nombre, cantidad, precio = datos
                    inventario[nombre] = {"cantidad": int(cantidad), "precio": float(precio)}
    return inventario

def guardar_inventario(inventario):
    with open(INVENTARIO_FILE, "w") as f:
        for nombre, datos in inventario.items():
            f.write(f"{nombre},{datos['cantidad']},{datos['precio']}\n")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    inventario = cargar_inventario()
    if nombre in inventario:
        inventario[nombre]["cantidad"] += cantidad
    else:
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    guardar_inventario(inventario)
    print("Producto agregado exitosamente.\n")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    inventario = cargar_inventario()
    if nombre in inventario:
        del inventario[nombre]
        guardar_inventario(inventario)
        print("Producto eliminado correctamente.\n")
    else:
        print("El producto no existe en el inventario.\n")

def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ")
    inventario = cargar_inventario()
    if nombre in inventario:
        cantidad = int(input("Nueva cantidad: "))
        precio = float(input("Nuevo precio: "))
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        guardar_inventario(inventario)
        print("Producto actualizado correctamente.\n")
    else:
        print("El producto no existe en el inventario.\n")

def ver_inventario():
    inventario = cargar_inventario()
    if inventario:
        print("\nInventario:")
        for nombre, datos in inventario.items():
            print(f"{nombre} - Cantidad: {datos['cantidad']}, Precio: ${datos['precio']:.2f}")
    else:
        print("El inventario está vacío.\n")

def menu():
    while True:
        print("\n--- Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Ver inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            ver_inventario()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
