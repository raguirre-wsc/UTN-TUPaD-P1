#TP N°1 Estructuras Secuenciales - Rodrigo Aguirre
def punto_1():
    print("Hola Mundo!")

def punto_2():
    nombre = input("Ingresa tu nombre: ")
    print(f"Hola {nombre}!")

def punto_3():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} a\u00f1os y vivo en {residencia}.")

def punto_4():
    import math
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    print(f"Área: {area}, Perímetro: {perimetro}")

def punto_5():
    segundos = int(input("Ingresa la cantidad de segundos: "))
    horas = segundos / 3600
    print(f"Equivale a {horas} horas")

def punto_6():
    numero = int(input("Ingresa un número: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def punto_7():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {num1 / num2}")

def punto_8():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Tu IMC es {imc}")

def punto_9():
    temp_celsius = float(input("Ingresa la temperatura en °C: "))
    temp_fahrenheit = (9/5) * temp_celsius + 32
    print(f"Equivale a {temp_fahrenheit} °F")

def punto_10():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio es {promedio}")
