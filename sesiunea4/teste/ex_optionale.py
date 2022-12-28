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
has_swaped = True
print(f'Lista de numere este: {alte_numere}')

while has_swaped:
    has_swaped = False
    for i in range(len(alte_numere)-1):
        if alte_numere[i] > alte_numere[i + 1]:
            swap = alte_numere[i]
            alte_numere[i] = alte_numere[i + 1]
            alte_numere[i + 1] = swap
            has_swaped = True

print(f'Lista sortata de numere este: {alte_numere}')


# TEST 1:
# incearca sa intelegi swap in variabile:
"""
a, b = 10, 2
print(f'Variabilele sunt: {a}, {b}')

# Varianta sa schimbi pe a in b
swap = a
a = b
b = swap
print(f'Dupa schimbare, a = {a} iar b = {b}')

# Varianta sa schimbi pe b in a
swap = b
b = a
a = swap
print(f'Dupa schimbare, b = {b} iar a = {a}')
"""


# TEST 2:
# incearca sa intelegi swap in liste:
"""
lst = [10, 2]
print(f'Lista este: {lst}')
swap = lst[0]
lst[0] = lst[1]
lst[1] = swap
print(f'Lista schimbata este: {lst}, index->0 = {lst[0]}, index->1 = {lst[1]}')
"""


# TEST 3:
# incearca sa folosesti swap iterand prin lista, verificand care nr este mai mare:
"""
lst = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
print(f'Lista este: {lst}')

for i in range(len(lst)-1):
    print(f'{lst[i]} danseaza cu {lst[i + 1]}')
    if lst[i] > lst[i + 1]:
        print(f'Nr {lst[i]} este mai mare ca {lst[i + 1]}')
        print(f'Nr {lst[i + 1]} coboara iar nr {lst[i]} urca')
        swap = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = swap
    else:
        print(f'Nr {lst[i]} ramane pe pozitie deoarece e mai mic ca {lst[i + 1]}')

print(f'Lista sortata: {lst}')
"""


# TEST 4:
# incearca sa folosesti iterand prin lista, verificand care nr este mai mare,
# pastreaza intr-o variabila daca s-a facut cel putin 1 schimbare:
"""
lst = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
print(f'Lista este: {lst}')

has_changed = True

while has_changed:
    has_changed = False
    for i in range(len(lst)-1):
        print(f'{lst[i]} danseaza cu {lst[i + 1]}')

        if lst[i] > lst[i + 1]:
            print(f'Nr {lst[i]} este mai mare ca {lst[i + 1]}')
            print(f'Nr {lst[i + 1]} coboara si se schimba cu nr {lst[i]}')
            swap = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = swap
            has_changed = True
        else:
            print(f'Nr {lst[i]} ramane pe pozitie deoarece e mai mic ca {lst[i + 1]}')

print(f'Lista sortata: {lst}')
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
