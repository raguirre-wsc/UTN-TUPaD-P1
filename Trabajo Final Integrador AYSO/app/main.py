import psycopg2
import time

#Espera hasta que el servicio de Postgres este operativo
time.sleep(5)

#Creamos conexion a la BD
conn = psycopg2.connect(
    host="db",
    dbname="recetas",
    user="user",
    password="password"
)

#Creamos un cursor para realizar consultas
cur = conn.cursor()

# Crear tabla si no existe
cur.execute("""
CREATE TABLE IF NOT EXISTS recetas (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    horario TEXT NOT NULL
)
""")
conn.commit()

print("RECETAS CARGADAS EN BD")

#Seleccionamos todo el contenido de la tabla y los mostramos linea por linea
cur.execute("SELECT * FROM recetas")
recetas = cur.fetchall()
for receta in recetas:
    print(receta)


#Hacemos un ciclo while para pedir nuevos datos hasta que el usuario termine el proceso
stop=""
while stop!="F":
    nombre = input("Ingrese el nombre de la receta: ")
    horario = input("Ingrese el horario de la receta: ")

    cur.execute("INSERT INTO recetas (nombre, horario) VALUES (%s, %s)", (nombre, horario))

    conn.commit()

    print("✅ Receta guardada correctamente.")

    stop=input("Ingrese F para finaliar o Enter para continuar: ")

#Termianmos el cursor y la conexion
cur.close()
conn.close()






