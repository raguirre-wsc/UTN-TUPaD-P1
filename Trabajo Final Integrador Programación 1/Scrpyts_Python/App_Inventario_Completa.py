import re

# Función merge sort para ordenar productos por código
def merge_sort(products):
    if len(products) > 1:
        mid = len(products) // 2
        left = products[:mid]
        right = products[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i]['codigo'] < right[j]['codigo']:
                products[k] = left[i]
                i += 1
            else:
                products[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            products[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            products[k] = right[j]
            j += 1
            k += 1

# Búsqueda binaria por código
def buscar_producto(productos):
    codigo = input("Ingrese el código del producto a buscar: ").upper()
    inicio = 0
    fin = len(productos) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        cod_actual = productos[medio]["codigo"]

        if cod_actual == codigo:
            print("Producto encontrado:")
            print(f"Código: {productos[medio]['codigo']}")
            print(f"Nombre: {productos[medio]['nombre']}")
            return productos[medio]
        elif codigo < cod_actual:
            fin = medio - 1
        else:
            inicio = medio + 1

    print("Producto no encontrado.")
    return None

# Funcion para agregar producto
def agregar_producto(productos):
    while True:
        codigo = input("Ingrese el código del producto (formato: 1 letra + 3 números, ej: A123): ").upper()
        if re.fullmatch(r"[A-Z][0-9]{3}", codigo):
            break
        else:
            print("Código inválido. Debe ser una letra seguida de 3 números (ej: B456). Intente de nuevo.")

    nombre = input("Ingrese el nombre del producto: ")
    productos.append({"codigo": codigo, "nombre": nombre.title()})
    merge_sort(productos)
    print("Producto agregado correctamente.")

# Funcion para eliminar producto
def eliminar_producto(productos):
    codigo = input("Ingrese el código del producto a eliminar: ").upper()
    inicio = 0
    fin = len(productos) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        cod_actual = productos[medio]["codigo"]

        if cod_actual == codigo:
            del productos[medio]
            print(f"Producto con código {codigo} eliminado.")
            return
        elif codigo < cod_actual:
            fin = medio - 1
        else:
            inicio = medio + 1

    print("Producto no encontrado.")

# Funcion para imprimir la lista completa
def imprimir_productos(productos):
    if not productos:
        print("La lista de productos está vacía.")
    else:
        print("Listado de productos:")
        for producto in productos:
            print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}")

# Menu principal
def menu(productos):
    while True:
        print("\n--- Menú de Productos ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Imprimir lista de productos")
        print("4. Buscar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            eliminar_producto(productos)
        elif opcion == "3":
            imprimir_productos(productos)
        elif opcion == "4":
            buscar_producto(productos)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# ---------------- Ejemplo de uso ----------------
productos = [
    {"codigo": "A200", "nombre": "Mouse"},
    {"codigo": "B100", "nombre": "Teclado"},
    {"codigo": "C300", "nombre": "Monitor"}
]

menu(productos)