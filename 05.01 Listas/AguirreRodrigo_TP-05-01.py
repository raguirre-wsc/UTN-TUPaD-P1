def ejercicio_1():
    multiplos_de_4 = list(range(4, 101, 4))
    print(multiplos_de_4)


def ejercicio_2():
    bandas_favoritas = ["SOAD", "CatupecuMachu", "Limpbizkit", "Deftones", "LosTipitos"]
    print(bandas_favoritas[-2])


def ejercicio_3():
    lista_vacia = []
    lista_vacia.append("python")
    lista_vacia.append("codigo")
    lista_vacia.append("aprendizaje")
    print(lista_vacia)


def ejercicio_4():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print(animales)

def ejercicio_5():
    #Remueve de la lista el número de mayor valor y luego imprime por consola la lista final.
    return None

def ejercicio_6():
    lista = list(range(10, 31, 5))
    print(lista[:2])

def ejercicio_7():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1] = "fiat"
    autos[2] = "renault"
    print(autos)


def ejercicio_8():
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print(dobles)


def ejercicio_9():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print(compras)


def ejercicio_10():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print(lista_anidada)