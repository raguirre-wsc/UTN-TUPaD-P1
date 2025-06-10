#TRABAJO PRACTICA FINAL INTEGRADOR - PROGRAMACION 1

#TESTO DE ALGORITMOS DE BUDQUEDA Y ORDENAMIENTO
#PRIMERO DEFINIMOS FUNCIONES CON ALGUNOS DE LOS DIFERENTES ALGORTIMOS QUE VAMOS A PROBAR
#BUSQUEDA:
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i][0] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio][0] == objetivo:
            return medio
        elif lista[medio][0] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

#ORDENAMIENTO:
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater)
    
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 
    return arr

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    arr = arr.copy()
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
    
#PASAMOS A GENERAR SETS DE DATOS DE PRUEBA, SE NOS OCURRIO SIMULAR STOCKS DE PRODUCTOS DE COMPUTACION

#IMPORTAMOS ALGUNAS LIBRERIAS
import random, itertools, time

#GENERAMOS UN ID ALFANUERICO UNICO PARA CADA PRODUCTO CON LA ESTRUCTURA "A000" POR EJEMPLO PARA EL PRIMER VALOR
# Letras de la A a la Z
letras = [chr(c) for c in range(65,91)]
# Números de 000 a 999 con formato fijo de 3 dígitos
numeros = [f"{i:03}" for i in range(1000)]
# Producto cartesiano: todas las combinaciones letra + número
id = [letra + numero for letra, numero in itertools.product(letras, numeros)]

#Generamos lista de productos usando comprehension lists, recorriendo los ids generados, agregamos campo de producto y lugar del almacen
productos = [[i,
            random.choice(["Mouse", "Teclado", "Monitor", "PC"]),
            random.choice(["Zona Sur","Zona Norte","CABA","Interior"])] 
            for i in id]

#TOMAMOS SUBSETS DE LISTA PRINCIPAL
set_chico = productos[:1000]
set_mediano = productos[:10000]
set_grande = productos[:26000]

#LOS DESORDENAMOS PARA LUEGO PROBAR LOS ALGORITMOS DE ORDENAMIENTO
random.shuffle(set_chico) 
random.shuffle(set_mediano)
random.shuffle(set_grande)

#HACEMOS PRUEBA DE RENDIMIENTO DE LOS ALGORITMOS DE ORDNEAMIENTO BUBBLE SORT y QUICKSORT:
#---QUICKSORT---
print("QUICKSORT")
#MUESTRA GRANDE
inicio_lineal = time.time()
lista_grande_ordenada= quicksort(set_grande)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Tiempo ejecucion con muestra grande: {tiempo_lineal}")

#MUESTRA MEDIANA
inicio_lineal = time.time()
lista_mediana_ordenada= quicksort(set_mediano)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Tiempo ejecucion con muestra mediana: {tiempo_lineal}")

#MUESTRA CHICA
inicio_lineal = time.time()
lista_chica_ordenada= quicksort(set_chico)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Tiempo ejecucion con muestra chica: {tiempo_lineal}")


#---BUBBLESORT---
print("BUBBLE SORT")
#MUESTRA GRANDE
inicio_lineal = time.time()
lista_grande_ordenada= bubble_sort(set_grande)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Tiempo ejecucion con muestra grande: {tiempo_lineal}")

#MUESTRA MEDIANA
inicio_lineal = time.time()
lista_mediana_ordenada= bubble_sort(set_mediano)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Tiempo ejecucion con muestra mediana: {tiempo_lineal}")

#MUESTRA CHICA
inicio_lineal = time.time()
lista_chica_ordenada= bubble_sort(set_chico)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Tiempo ejecucion con muestra chica: {tiempo_lineal}")



#TESTEAMOS LOS ALGORITMOS DE BUSQUEDA
#---BUSQUEDA LINEAL---
print("LINEAL")
#MUESTRA GRANDE
inicio_lineal = time.time()
indice_busqueda = busqueda_lineal(lista_grande_ordenada,"Z900")
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Tiempo ejecucion con muestra grande: {tiempo_lineal}, elemento encontrado en {indice_busqueda}")

#---BUSQUEDA BINARIA---
print("BINARIA")
#MUESTRA GRANDE
inicio_lineal = time.time()
indice_busqueda= busqueda_binaria(lista_grande_ordenada,"Z900")
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Tiempo ejecucion con muestra grande: {tiempo_lineal}, elemento encontrado en {indice_busqueda}")
