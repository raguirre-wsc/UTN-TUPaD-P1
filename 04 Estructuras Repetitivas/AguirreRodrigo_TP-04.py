import random

def ejercicio_1():
    for i in range(101):
        print(i)
    

def ejercicio_2():
    num = input("Ingrese un número entero: ")
    print("Cantidad de dígitos:", len(num.lstrip('-')))
    

def ejercicio_3():
    suma = 0
    a = int(input("Ingrese el primer número: ")) + 1
    b = int(input("Ingrese el segundo número: "))
    for i in range(a,b):
        suma += i
    print("La suma es:", suma)


def ejercicio_4():
    total = 0
    while True:
        num = int(input("Ingrese un número: "))
        if num == 0:
            break
        total += num
    print("La suma total es:", total)
    

def ejercicio_5():
    secreto = random.randint(0, 9)
    intentos = 0
    while True:
        respuesta = int(input("Adivina el número del 0-9: "))
        intentos += 1
        if respuesta == secreto:
            print(f"¡Ganaste! Adivinaste en {intentos} intentos.")
            break
    

def ejercicio_6():
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)
    

def ejercicio_7():
    suma = 0
    n = int(input("Ingrese un número entero positivo: ")) + 1
    for i in range(0,n):
        suma += i
    print("La suma total es:", suma)
    

def ejercicio_8():
    cantidad = 100
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    for i in range(cantidad):
        num = int(input("Ingrese un número: "))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1

    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")
    

def ejercicio_9():
    cantidad = 3  
    total = 0

    for i in range(cantidad):
        num = int(input("Ingrese un número: "))
        total += num

    media = total / cantidad
    print(f"La media es: ", media)
    

def ejercicio_10():
    numero = input("Ingrese un número: ")
    invertido = numero[::-1]
    print(f"Número invertido: ", invertido)
    