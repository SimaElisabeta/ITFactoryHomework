# 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# a) Afiseaz-o
# b) Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# c) Printeaza varianta actuala (inversata)
# d) Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii
# inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta
# automat)
# e) Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
# Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista
# sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si
# permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne
# dorim in acel moment.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

# a)
print(note_muzicale)

# b)
note_muzicale = note_muzicale[::-1]

# c)
print(note_muzicale)

# d)
note_muzicale.reverse()

# e)
print(note_muzicale)

# 2. Utilizand aceeasi lista, de cate ori apare 'do'?
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

print(note_muzicale.count('do'))

# 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.
l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]

l3 = l1 + l2
print(l3)
l1.extend(l2)
print(l1)

# 4. Sortati si afisati lista generata la ex anterior. Stergeti numarul 0 folosind o functie. Afisati iar lista
l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]

l3 = l1 + l2
print(f"Lista inainte de sortare: {l3}")
l3.sort()
print(f"Lista dupa sortare:       {l3}")

l3.remove(0)
print(f"Lista fara numarul 0:     {l3}")

# 5. Folosind un if verificati lista generata la ex3 si afisati:
#  - Lista este goala
#  - Lista nu este goala
l = [3, 1, 0, 2, 6, 5, 4]

if l:   # sau if len(l1)!=0: sau if l1 != []
    print('Lista nu este goala')
else:
    print('Lista este goala')


# 6. Folositi o functie care sa goleasca lista de la ex3
l = [3, 1, 0, 2, 6, 5, 4]
print(f"Lista inainte de golire: {l}")
l.clear()  # del l[:]
print(f"Lista dupa golire: {l}")

# 7. Copy paste la ex 5. Verificati inca o data. Acum ar trebui sa se afiseze ca lista e goala.
if l:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# 8.Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}. Folositi o functie ca sa afisati Elevii (cheile)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

print(list(dict1.keys()))

# 9. Printati cei 3 elevi si notele lor.
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie.

# v1 afisarea pentru un elev introdus de la tastatura
student = input("Introduceti numele elevului pentru care vreti nota: ")
print(f"{student} a luat nota {dict1[student]}")

# v2 (afisarea notelor tuturor cu for pe care inca nu l`am invatat :D)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
for key in dict1:
    print(f"{key} a luat nota {dict1[key]}")

# sau
for elev, nota in dict1.items():
    print(f'{elev} a luat nota {nota}')

# 10. Dorel a facut contestatie si a primit 6. Modificati nota lui Dorel in 6. Printati nota dupa modificare.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

dict1['Dorel'] = 6
print(dict1['Dorel'])

# 11.Gigel se transfera din clasa. Cautati o functie care sa il stearga. Vine un coleg nou. Adaugati Ionica, cu nota 9.
# Printati noii elevi.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 6}

del dict1['Gigel']
dict1['Ionica'] = 9
print(dict1)

# IN ECHIPA
# 1. Set zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}, weekend = {'sambata', 'duminica'}.
# Adaugati in zilele_sapt ‘luni’. Afisati zile_sapt
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(zile_sapt)

# 2.Folositi un if si verificati daca:
# - Weekend este un subset al zilelor din sapt
# - Weekend nu este un subset al zilelor din sapt
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

if weekend.issubset(zile_sapt):
    print(f"Weekend e subset al zile_sapt")
else:
    print(f"Weekend nu e subset al zile_sapt")

# 3. Afisati diferentele dintre aceste 2 seturi
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

print(zile_sapt - weekend)

# sau
print(zile_sapt.difference(weekend))

# 4. Afisati intersectia elementelor din aceste 2 seturi
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

print(zile_sapt & weekend)

# sau
print(weekend.intersection(zile_sapt))
print(zile_sapt.intersection(weekend))

# OPTIONAL
# 1. Ne imaginam o echipa de fotbal pt teren sintetic. 3 Schimbari maxime admise.
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3

# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’

# Testati codul cu diferite valori

# Google search hint
# “how to check if item is in list python”
playing = ["Leo", "Cristiano", "Erling", "Kylian", "Gianluigi"]
substitutes = ["Sergi", "Ferran", "Memphis", "Ansu", "Frenkie"]
substitutes_max = 3

substitutes_done = int(input("Introduceti cate schimbari au fost efectuate pana acum dintr-un maxim de 3: "))
player_to_change = input(f"Introduceti numele unui jucator pe care sa il schimbati dintre {playing}:")
if player_to_change in playing:
    if substitutes_done < substitutes_max:
        player_in = substitutes.pop()
        playing.remove(player_to_change)
        playing.append(player_in)
        substitutes_done += 1
        print(f"A intrat {player_in}, a iesit {player_to_change}, mai aveti {substitutes_max - substitutes_done} schimbari")
    print(f"Mai aveti {substitutes_max - substitutes_done} schimbari ")
else:
    print(f"Nu se poate efectua schimbarea, deoarece jucatorul {player_to_change} nu e in teren!")