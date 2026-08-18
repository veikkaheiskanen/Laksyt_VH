sukupuoli = input("Anna sukupuoli (mies/nainen): ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "mies" and hemoglobiini <= 134:
    print("Hemoglobiini on alhainen")
elif sukupuoli == "mies" and hemoglobiini >= 195:
    print("Hemoglobiini on korkea")
elif sukupuoli == "mies":
    print("Hemoglobiini on normaali")

if sukupuoli == "nainen" and hemoglobiini <= 117:
    print("Hemoglobiini on alhainen")
elif sukupuoli == "nainen" and hemoglobiini >= 175:
    print("Hemoglobiini on korkea")
elif sukupuoli == "nainen":
    print("Hemoglobiini on normaali")