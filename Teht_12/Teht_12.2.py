import requests

api_avain = "oma_api_avain"

def kelvin_celsius(kelvin):
    return kelvin - 273.15

paikkakunta = input("Anna paikkakunnan nimi: ")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}&lang=fi"
vastaus = requests.get(pyyntö)

if vastaus.status_code == 200:
    json_vastaus = vastaus.json()
    sää = json_vastaus["weather"][0]["description"]
    lämpötila = kelvin_celsius(json_vastaus["main"]["temp"])
    print(f"Säätila: {sää}")
    print(f"Lämpötila: {lämpötila:.1f} °C")
else:
    print("Paikkakuntaa ei löytynyt")