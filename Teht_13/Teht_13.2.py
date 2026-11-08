import mysql.connector
from flask import Flask

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='your_new_password',
         autocommit=True
         )

app = Flask(__name__)

def hae_lentokenttä(icao_koodi):
    sql = "SELECT name, municipality from airport where IDENT=%s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao_koodi,))
    tulos = kursori.fetchone()
    return tulos

@app.route("/kenttä/<icao>")
def kenttä(icao):
    tulos = hae_lentokenttä(icao.upper())

    if tulos is None:
        return {"virhe": "Lentokenttää ei löytynyt"}, 404

    vastaus = {
        "ICAO": icao.upper(),
        "Name": tulos[0],
        "Municipality": tulos[1]
    }
    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)