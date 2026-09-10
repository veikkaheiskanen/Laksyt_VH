import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='your_new_password',
         autocommit=True
         )

def hae_tietokannasta_icao(icao_koodi):
    sql = f"SELECT name, municipality from airport where IDENT='{icao_koodi}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        print(f"Lentokentän nimi: {rivi[0]} sekä sijaintikunta: {rivi[1]}")

kysymys_icao_koodi = input("Anna lentoaseman ICAO-koodi: ")
hae_tietokannasta_icao(kysymys_icao_koodi)