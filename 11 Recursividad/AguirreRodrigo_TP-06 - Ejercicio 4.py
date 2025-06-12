def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

numero_decimal = int(input("Ingrese un número decimal para convertir a binario: "))
binario = decimal_a_binario(numero_decimal)
# Asegurarse de que no quede vacío si el número es 0
binario = binario if binario != "" else "0"
print(f"El número {numero_decimal} en binario es: {binario}")