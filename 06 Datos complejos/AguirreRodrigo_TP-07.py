def ejercicio_frutas():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

    # Agregar frutas
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800

    frutas = list(precios_frutas.keys())
    print(frutas)  # ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']

def agenda_telefonica():
    agenda = {}
    
    # Cargar 5 contactos
    for i in range(5):
        nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
        numero = input(f"Ingresá el número de {nombre}: ")
        agenda[nombre] = numero

    # Consultar un contacto
    buscar = input("¿A qué contacto querés buscar? Ingresá el nombre: ")
    if buscar in agenda:
        print(f"El número de {buscar} es {agenda[buscar]}")
    else:
        print("Contacto no encontrado.")

def analizar_frase():
    frase = input("Ingresá una frase: ").lower()
    palabras = frase.split()

    # Palabras únicas
    palabras_unicas = set(palabras)
    print("Palabras únicas:", palabras_unicas)

    # Frecuencia de palabras
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    print("Frecuencia de palabras:", frecuencia)

def cargar_alumnos_y_mostrar_promedios():
    alumnos = {}

    for _ in range(3):
        nombre = input("Ingresá el nombre del alumno: ")
        notas = []
        for i in range(1, 4):
            nota = float(input(f"Ingresá la nota {i} de {nombre}: "))
            notas.append(nota)
        alumnos[nombre] = tuple(notas)

    print("\nPromedios de cada alumno:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio:.2f}")

def analizar_aprobados():
    # Sets de ejemplo (pueden reemplazarse por input si querés hacerlo interactivo)
    parcial1 = {"Ana", "Luis", "María", "Pedro"}
    parcial2 = {"Luis", "Pedro", "Sofía", "Julián"}

    # Aprobados en ambos parciales (intersección)
    ambos = parcial1 & parcial2
    print("Aprobaron ambos parciales:", ambos)

    # Aprobó solo uno (diferencia simétrica)
    solo_uno = parcial1 ^ parcial2
    print("Aprobaron solo uno de los dos:", solo_uno)

    # Aprobó al menos uno (unión)
    al_menos_uno = parcial1 | parcial2
    print("Aprobaron al menos un parcial:", al_menos_uno)

def gestionar_stock():
    stock_productos = {
        "pan": 10,
        "leche": 20,
        "huevos": 30
    }

    producto = input("Ingresá el nombre del producto: ").lower()

    if producto in stock_productos:
        print(f"Stock actual de {producto}: {stock_productos[producto]}")
        try:
            cantidad = int(input(f"¿Cuántas unidades querés agregar a {producto}? "))
            stock_productos[producto] += cantidad
            print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
        except ValueError:
            print("Debe ingresar un número válido.")
    else:
        try:
            cantidad = int(input(f"{producto} no existe. ¿Cuántas unidades querés agregar como nuevo producto? "))
            stock_productos[producto] = cantidad
            print(f"{producto} agregado con stock: {cantidad}")
        except ValueError:
            print("Debe ingresar un número válido.")

    print("\nStock actualizado:")
    for prod, cantidad in stock_productos.items():
        print(f"{prod}: {cantidad}")
    
def agenda_eventos():
    agenda = {
        ("lunes", "10:00"): "Reunión de equipo",
        ("martes", "14:00"): "Llamada con cliente",
        ("miércoles", "09:00"): "Revisión de informes"
    }

    dia = input("Ingresá el día (por ejemplo, lunes): ").lower()
    hora = input("Ingresá la hora (por ejemplo, 10:00): ")

    clave = (dia, hora)

    if clave in agenda:
        print(f"Evento en {dia} a las {hora}: {agenda[clave]}")
    else:
        print(f"No hay eventos agendados para {dia} a las {hora}.")

def invertir_diccionario_capitales():
    paises_a_capitales = {
        "Argentina": "Buenos Aires",
        "Brasil": "Brasilia",
        "Chile": "Santiago",
        "Uruguay": "Montevideo",
        "Paraguay": "Asunción"
    }

    capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}

    print("Diccionario original:")
    print(paises_a_capitales)
    print("\nDiccionario invertido:")
    print(capitales_a_paises)