def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular los factoriales hasta ese número: "))
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")