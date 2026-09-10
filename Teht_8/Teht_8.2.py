import mysql.connector

yhteys = mysql.connector.connect (
        host='localhost',
        port=3306,
        database='flight_game',
        user='root',
        password='my_new_password',
        autocommit=True
        )

def hae_maakoodi(koodi):
    sql = f"select type, COUNT(type) from airport where iso_country = '{maa_kysymys}' group by type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos_numero = kursori.fetchall()
    for luku in tulos_numero:
        print(luku)

maa_kysymys = input("Anna maa: ")
hae_maakoodi(maa_kysymys)