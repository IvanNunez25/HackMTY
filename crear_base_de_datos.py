import sqlite3

conn = sqlite3.connect('banorte_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS fondo_de_inversion (
                    id INTEGER PRIMARY KEY,
                    fondo TEXT NOT NULL,
                    caracteristicas TEXT NOT NULL
                )''')

fondos = [
    ("NTEDIG", "Familia_Basicos corto_plazo conservadora disponiblilidad_diaria ambiental inversion_global "),
    ("NTECT", "Familia_Basicos corto_plazo conservadora disponiblilidad_diaria inversion_global sociedad "),
    ("NTEPZO", "Familia_Basicos corto_plazo inversion_pacifico ambiental "),
    ("NTED", "Familia_Estrategicos mediano_plazo alto_crecimiento empresas_jovenes mediano_riesgo "),
    ("NTE1", "Familia_Estrategicos mediano_plazo riesgo_bajo gobierno "),
    ("NTE2", "Familia_Estrategicos mediano_plazo riesgo_moderado "),
    ("NTE3", "Familia_Estrategicos mediano_plazo riesgo_alto "),
    ("NTEDLS", "Familia_Especializados largo_plazo "),
    ("NTEDLS+", "Familia_Especializados largo_plazo alta_calidad riesgo_bajo gobierno "),
    ("NTEIPC+", "Familia_Especializados largo_plazo inversion_global sociedad "),
    ("NTEESG", "Familia_Especializados largo_plazo inversion_global sociedad ambiental gobierno"),
]

for fondo, caracteristicas in fondos:
    cursor.execute("INSERT INTO fondo_de_inversion (fondo, caracteristicas) VALUES (?, ?)", (fondo, caracteristicas))

conn.commit()
conn.close()


