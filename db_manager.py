import sqlite3

DB_PATH = "ganado.db"

def conectar():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabla principal de animales
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS animales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            raza TEXT,
            edad INTEGER,
            peso REAL,
            sexo TEXT,
            fecha_nacimiento TEXT,
            salud TEXT,
            observaciones TEXT
        )
    """)

    # Tabla de razas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS razas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE
        )
    """)

    # 🩺 Nueva tabla veterinaria
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tratamientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal TEXT,
            diagnostico TEXT,
            medicamento TEXT,
            dosis TEXT,
            fecha TEXT
        )
    """)

    conn.commit()
    conn.close()


# ----- CRUD Animales -----
def agregar_raza(raza):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO razas (nombre) VALUES (?)", (raza,))
    except sqlite3.IntegrityError:
        pass
    conn.commit()
    conn.close()


def obtener_razas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM razas")
    razas = [r[0] for r in cursor.fetchall()]
    conn.close()
    return razas


def agregar_animal(nombre, raza, edad, peso, sexo, fecha_nacimiento, salud, observaciones):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO animales (nombre, raza, edad, peso, sexo, fecha_nacimiento, salud, observaciones)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nombre, raza, edad, peso, sexo, fecha_nacimiento, salud, observaciones))
    conn.commit()
    conn.close()
    agregar_raza(raza)


def obtener_animales():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animales")
    animales = cursor.fetchall()
    conn.close()
    return animales


# ----- CRUD Veterinaria -----
def agregar_tratamiento(animal, diagnostico, medicamento, dosis, fecha):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tratamientos (animal, diagnostico, medicamento, dosis, fecha)
        VALUES (?, ?, ?, ?, ?)
    """, (animal, diagnostico, medicamento, dosis, fecha))
    conn.commit()
    conn.close()


def obtener_tratamientos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tratamientos")
    tratamientos = cursor.fetchall()
    conn.close()
    return tratamientos
