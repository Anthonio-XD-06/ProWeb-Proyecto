import sqlite3

conn = sqlite3.connect('base.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Agrega un usuario de prueba
c.execute("INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)", ('prueba', '1234'))

conn.commit()
conn.close()
