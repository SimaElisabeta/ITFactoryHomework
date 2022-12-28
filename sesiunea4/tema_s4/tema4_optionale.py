import random

"""1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
a) Itereaza prin listă alte_numere
b) Populează corect celelalte liste
c) Afișează cele 4 liste la final
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []                # % 2 == 0
numere_impare = []              # % 2 >= 1
numere_pozitive = []            # i > 0
numere_negative = []            # i < 0

for i in range(len(alte_numere)):
    if alte_numere[i] % 2 == 0:
        numere_pare.append(alte_numere[i])
    else:
        numere_impare.append(alte_numere[i])
    if alte_numere[i] > 0:
        numere_pozitive.append(alte_numere[i])
    elif alte_numere[i] < 0:
        numere_negative.append(alte_numere[i])

print(f'Lista de numere este: {alte_numere}')
print(f'Numere pare: {numere_pare}')
print(f'Numere impare: {numere_impare}')
print(f'Numere pozitive: {numere_pozitive}')
print(f'Numere negative: {numere_negative}')


"""2. Aceeași listă:
Ordonează crescător lista fară să folosești sort. Te poți inspira vizual de aici: link...
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
schimbare_facuta = True
print(f'Lista de numere este: {alte_numere}')

while schimbare_facuta:
    schimbare_facuta = False
    for i in range(len(alte_numere)-1):
        if alte_numere[i] > alte_numere[i + 1]:
            schimb = alte_numere[i]
            alte_numere[i] = alte_numere[i + 1]
            alte_numere[i + 1] = schimb
            schimbare_facuta = True

print(f'Lista sortata de numere este: {alte_numere}')


# TEST explicit pe exemplul cu dans:
# iterand prin lista descriu toate schimbarile/evenimentele
# verific care nr este mai mare, folosind swap fac shimbul intre numere
"""
dansatori = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
print(f'Lista de dansatori este: {dansatori}')

for i in range(len(dansatori)-1):
    print(f'{dansatori[i]} danseaza cu {dansatori[i + 1]}')
    if dansatori[i] > dansatori[i + 1]:
        print(f'Nr {dansatori[i]} este mai mare ca {dansatori[i + 1]}')
        print(f'Nr {dansatori[i + 1]} coboara iar nr {dansatori[i]} urca')
        swap = dansatori[i]
        dansatori[i] = dansatori[i + 1]
        dansatori[i + 1] = swap
    else:
        print(f'Nr {dansatori[i]} ramane pe pozitie deoarece e mai mic ca {dansatori[i + 1]}')

print(f'Lista sortata de dansatori: {dansatori}')

"""


"""3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 3', 20 * '-')
numar_secret = random.randint(1, 30)
numar_ghicit = None

while True:
    numar_ghicit = int(input('Alege un numar între 1 și 30: '))
    if 1 <= numar_ghicit <= 30:
        if numar_ghicit < numar_secret:
            print(f'Nr secret e mai mare')
        elif numar_ghicit > numar_secret:
            print(f'Nr secret e mai mic')
        else:
            print('Felicitări! Ai ghicit!')
            break
    else:
        print('Atentie, trebuie sa alegi un numar intre 1 si 30, mai incearca!')