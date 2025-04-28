# Conversión de Números:
# Desarrollen un programa que convierta números decimales a binarios.
# Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.

# Inputs:
# - Números Decimales -> int

# Output:
# - Números Binarios -> int 

# Liberias a utilizar
import math

# Definimos las variables, las incializamos vacias
num_input = ""
num_output = ""

# Definimos algunas funciones que nos seran útiles mas adelante
# La siguiente función la utilizaremos para invertir los bits de un número binario, devuelve 1 si se le paso 0 a la funcion
# y viceversa 
def inversion_bit(bit):
    return "1" if bit == "0" else "0"

# Mensaje de inicio
print("Bienvenido al programa de conversion a binario!")
print("Ingrese un número decimal para su conversión:")

# En esta sección solicitamos el input del número decimal y hacemos una validación del input
while True:
    num_input = input()
    # Intentamos parcear el numero ingresado a int. Si no es posible, levantamos una excepción y
    # pedimos que ingrese un número valido
    try:
        num_input = int(num_input)
        print("Input correcto, convirtiendo...")
        break
    except Exception:
        print("Ingrese un un numero valido")


# Creamos el algoritmo de pasaje de decimal a binario
# Primero evaluamos si el número ingresado es negativo o positivo y lo almacenamos en una variable booleana.
if num_input < 0:
    negativo = True
else:
    negativo = False

# Guardamos el valor absoluto del número
num_input = abs(num_input)

# Definimos la variable "residuo" que ira almacenando cada bit durante la conversión
residuo = None

# Hacemos división sucesiva x 2 hasta que el cociente se iguale a 0
while num_input != 0:
    residuo = num_input % 2
    num_input = math.floor(num_input / 2)
    num_output = num_output + str(residuo)
# Una vez terminado de correr el while, invertimos el reusltado para que los bits queden en la posición correcta.    
num_output = num_output[::-1]

# Si el número a convertir es negativo representamos el complemento a 2 con la menor cantidad de bits posibles    
# Primero hacemos complemento a 1
complemento1 = ""
if negativo:
    # Agregamos padding de un bit para poder representar el signo
    num_output = "0" + num_output
    # Recorremos cada bit del número binario invirtiendolos
    for i in num_output:
        complemento1 += inversion_bit(i)

# Hacemos complmeneto a 2
# Para el algoritmo de suma recorremos el complmeneto 1, la idea para lidiar con el carry es 
# ver si el bit anterior (i+1) al analizado (i) es 0 o 1.
# Si (i+1) es 0 quiere decir que hay carry y al bit en la posición i tengo que sumarle 1, en caso
# contrario el ciclo termina.

    complemento1 = list(complemento1)
    complemento2 = complemento1.copy()
    primer_bit = len(complemento1)-1
    ultimo_bit = -1

    for i in range(primer_bit, ultimo_bit, -1):
        if i == primer_bit:
                complemento2[i]=inversion_bit(complemento2[i])
        elif 0 < i < len(complemento2)-1:
            if complemento2[i+1] == "1":
                break
            else:
                if complemento2[i] == "1":
                    complemento2[i]=inversion_bit(complemento2[i])
                else:
                    complemento2[i]=inversion_bit(complemento2[i])
                    break
        elif i == 0:
            # Si hubo carry hasta el último bit, hacemos 0 e insertamos un bit mas para que quede 10
            if complemento1[i] == "1":
                complemento2[i]=inversion_bit(complemento2[i])
                complemento2.insert(0,"1")   
    num_output="".join(complemento2)

# Finalmente imprimos el resultado de la conversión.
print(f"Número decimal: {num_input} -> Número binario: {num_output}")

    











