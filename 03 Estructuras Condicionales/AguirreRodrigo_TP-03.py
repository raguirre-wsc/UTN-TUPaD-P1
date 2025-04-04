import random
from statistics import mode, median, mean

def ejercicio_1():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Es mayor de edad")

def ejercicio_2():
    nota = float(input("Ingrese su nota: "))
    if (nota >= 6):
        print("Aprobado" )
    else:
        print ("Desaprobado")

def ejercicio_3():
    num = int(input("Ingrese un número par: "))
    if (num % 2 == 0): 
        print("Ha ingresado un número par")
    else: 
        print("Por favor, ingrese un número par")

def ejercicio_4():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

def ejercicio_5():
    password = input("Ingrese una contraseña: ")
    if (8 <= len(password) <= 14):
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

def ejercicio_6():
    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    if media > mediana > moda:
        print("Sesgo positivo")
    elif media < mediana < moda:
        print("Sesgo negativo")
    else:
        print("Sin sesgo")

def ejercicio_7():
    frase = input("Ingrese una frase o palabra: ")
    if (frase[-1].lower() in "aeiou"): 
        print(frase + "!") 
    else:
        print(frase)

def ejercicio_8():
    nombre = input("Ingrese su nombre: ")
    opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: ")
    if (opcion == "1"):
        print(nombre.upper())
    elif (opcion == "2"):
        print(nombre.lower())
    elif (opcion == "3"):
        print(nombre.title())

def ejercicio_9():
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve")
    elif magnitud < 4:
        print("Leve")
    elif magnitud < 5:
        print("Moderado")
    elif magnitud < 6:
        print("Fuerte")
    elif magnitud < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")

def ejercicio_10():
    hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
    mes = int(input("Ingrese el número del mes (1-12): "))
    dia = int(input("Ingrese el día del mes: "))
    if hemisferio == "S":
        if ((mes == 12 and 21>=dia) or mes in [1,2] or (mes == 3 and 20<=dia)):
            print("Verano")
        elif ((mes == 3 and 21>=dia) or mes in [4,5] or (mes == 6 and 20<=dia)):
            print("Otoño")
        elif ((mes == 6 and 21>=dia) or mes in [10,11] or (mes == 9 and 20<=dia)):
            print("Invierno")
        elif ((mes == 9 and 21>=dia) or mes in [4,5] or (mes == 12 and 20<=dia)):
            print("Primavera")
    else:
        if ((mes == 12 and 21>=dia) or mes in [1,2] or (mes == 3 and 20<=dia)):
            print("Invierno")
        elif ((mes == 3 and 21>=dia) or mes in [4,5] or (mes == 6 and 20<=dia)):
            print("Primavera")
        elif ((mes == 6 and 21>=dia) or mes in [10,11] or (mes == 9 and 20<=dia)):
            print("Verano")
        elif ((mes == 9 and 21>=dia) or mes in [4,5] or (mes == 12 and 20<=dia)):
            print("Otoño")




