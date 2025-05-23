import sqlite3

conn = sqlite3.connect('finanzas.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS tarjetas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT,
    fecha_corte TEXT,
    fecha_pago TEXT,
    debe REAL
)""")

conn.commit()
conn.close()
print("Base de datos creada como 'finanzas.db'")
