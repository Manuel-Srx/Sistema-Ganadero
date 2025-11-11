import sqlite3
import os

# Crear carpeta si no existe
if not os.path.exists("database"):
    os.makedirs("database")

# Función para conectar a la base de datos
def conectar():
    conn = sqlite3.connect("database/ganado.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS animales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            nombre TEXT,
            raza TEXT,
            peso REAL,
            edad INTEGER,
            estado TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Función para agregar un nuevo animal
def agregar_animal(codigo, nombre, raza, peso, edad, estado):
    conn = sqlite3.connect("database/ganado.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO animales (codigo, nombre, raza, peso, edad, estado)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (codigo, nombre, raza, peso, edad, estado))
    conn.commit()
    conn.close()

# Función para obtener todos los animales
def obtener_animales():
    conn = sqlite3.connect("database/ganado.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animales")
    datos = cursor.fetchall()
    conn.close()
    return datos
