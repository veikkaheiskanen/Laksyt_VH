import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='my_new_password',
         autocommit=True
         )

def hae_tietokannasta_icao(kysymys):
    sql = f"SELECT latitude_deg, longitude_deg from airport where IDENT='{kysymys}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    return tulos

def laske_etaisyys(piste1, piste2):
    print(f"Lentokenttien etäisyys on: {geodesic(piste1, piste2).km:.2f} kilometriä")

ensimmainen_koodi = input("Anna 1. lentoaseman ICAO-koodi: ")
ensimmaiset = hae_tietokannasta_icao(ensimmainen_koodi)
toinen_koodi = input("Anna 2. lentoaseman ICAO-koodi: ")
toiset = hae_tietokannasta_icao(toinen_koodi)

laske_etaisyys(ensimmaiset, toiset)