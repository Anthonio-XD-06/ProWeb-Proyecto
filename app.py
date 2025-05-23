from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

def init_db():
    if not os.path.exists("finanzas.db"):
        with sqlite3.connect("finanzas.db") as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS tarjetas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero TEXT,
                fecha_corte TEXT,
                fecha_pago TEXT,
                debe REAL
            )""")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tarjetas", methods=["GET"])
def get_tarjetas():
    with sqlite3.connect("finanzas.db") as conn:
        c = conn.cursor()
        c.execute("SELECT numero, fecha_corte, fecha_pago, debe FROM tarjetas")
        tarjetas = [{"numero": row[0], "fecha_corte": row[1], "fecha_pago": row[2], "debe": row[3]} for row in c.fetchall()]
        return jsonify(tarjetas)

@app.route("/agregar_tarjeta", methods=["POST"])
def agregar_tarjeta():
    data = request.get_json()
    with sqlite3.connect("finanzas.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO tarjetas (numero, fecha_corte, fecha_pago, debe) VALUES (?, ?, ?, ?)",
                  (data["numero"], data["fecha_corte"], data["fecha_pago"], data["debe"]))
        conn.commit()
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    init_db()
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
