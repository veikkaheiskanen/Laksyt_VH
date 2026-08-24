value = 0
lowest = 999999999
highest = -999999999
while value != "":
    value = input("Syötä luku: ")
    if value == "":
        print(f"Pienin luku: {lowest}")
        print(f"Suurin luku: {highest}")
    else:
        if int(value) < lowest:
            lowest = int(value)
        elif int(value) > highest:
            highest = int(value)