import psycopg2
import time

time.sleep(5)

conn = psycopg2.connect(
    host="db",
    dbname="recetas",
    user="user",
    password="password"
)
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

print("RESETAS CARGADAS EN BD")

cur.execute("SELECT * FROM recetas")
recetas = cur.fetchall()
for receta in recetas:
    print(receta)

stop=""

while stop!="F":
    nombre = input("Ingrese el nombre de la receta: ")
    horario = input("Ingrese el horario de la receta: ")

    cur.execute("INSERT INTO recetas (nombre, horario) VALUES (%s, %s)", (nombre, horario))

    conn.commit()

    print("✅ Receta guardada correctamente.")

    stop=input("Ingrese F para finaliar o Enter para continuar: ")

cur.close()
conn.close()






