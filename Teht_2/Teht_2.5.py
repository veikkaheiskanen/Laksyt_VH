leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

massa = luodit * 13.3 + naulat * 13.3 * 32 + leiviskat * 13.3 * 32 * 20

kg = massa // 1000
g = massa % 1000

print(f"Massa nykymitoissa on: {kg} kg ja {g:0.2f} g")