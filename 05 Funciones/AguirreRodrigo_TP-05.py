import math

# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return suma, resta, multiplicacion, division

# Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3