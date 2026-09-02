def karsi_parittomat(luvut):
    karsittu = []

    for luku in luvut:
        if luku % 2 == 0:
            karsittu.append(luku)

    return karsittu


luvut = [1, 2, 3, 4, 5, 6, 7, 8]

karsittu = karsi_parittomat(luvut)

print(luvut)
print(karsittu)