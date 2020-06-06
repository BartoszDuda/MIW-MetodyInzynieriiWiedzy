def indeksy(a, lis1):
    indeks = str((lis1[a])["Indeks"])
    return indeks


def imiona(a, lis1):
    imie = str((lis1[a])["Imie"])
    return imie


def wyswietlanie(rozmiar_tablicy):
    d = ""
    for i in range(rozmiar_tablicy):
        c = "| Indeks: " + indeksy(i, lista) + " | Imię: " + imiona(i, lista) + " |"
        d = d + c
    print(d)


lista = ({"Indeks": 12223, "Imie": "Bartosz"},
         {"Indeks": 13544, "Imie": "Michal"},
         {"Indeks": 15223, "Imie": "Kamil"})

wyswietlanie(3)
