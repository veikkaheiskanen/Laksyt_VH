vuosi = float(input("Anna Vuosiluku: "))

if(vuosi % 4 == 0) or (vuosi % 100 != 0 and vuosi % 400 == 0):
    print("Vuosiluku on karkausvuosi.")
else:
    print("Vuosiluku ei ole karkausvuosi.")