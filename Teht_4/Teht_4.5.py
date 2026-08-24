usr_name = "python"
pswd = "rules"
tries = 0

while tries < 5:
    name = input("Syötä nimesi: ")
    password = input("Syötä salasanasi: ")

    if name == usr_name and password == pswd:
        print(f"Tervetuloa")
        break
    else:
        print("Pääsy evätty")
        tries += 1