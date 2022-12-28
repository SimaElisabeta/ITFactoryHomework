"""
1. Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
●‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
nr = 0
print(5 * '-', 'a) for', 5 * '-')
for i in range(len(masini)):
    nr += 1
    print(f'{str(nr)}. Mașina mea preferată este {masini[i]}')

nr = 0
print(5 * '-', 'b) for each', 5 * '-')
for masina in masini:
    nr += 1
    print(f'{str(nr)}. Mașina mea preferată este {masina}')

nr = 0
index = 0
print(5 * '-', 'c) while', 5 * '-')
while index < len(masini):
    nr += 1
    print(f'{str(nr)}. Mașina mea preferată este {masini[index]}')
    index += 1


"""
2. Aceeași listă:
Folosește un for else:
a) În for
- Modifică elementele din listă astfel încât să fie scrise cu majuscule,
exceptând primul și ultimul.
b) În else:
- Printează lista.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# prima incercare:
# for masina in masini:
#     if masini.index(masina) == 0 or masini.index(masina) == len(masini) - 1:
#         continue
#     masini[masini.index(masina)] = masina.upper()

for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
else:
    print(masini)


"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
a) Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
b) Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 3', 20 * '-')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print(f'Am găsit mașina dorită de dvs!')
        break
    else:
        print(f'Am găsit mașina {masina}. Mai căutam...')


"""
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
a) Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
b) Printează 'S-ar putea să vă placă mașina x'.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 4', 20 * '-')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
print('Buna ziua! Cu siguranta va putem ajuta sa gasiti o masina pe placul dvs. Avem o gama de top.')

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    print(f'S-ar putea să vă placă mașina: {masina}')


"""
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Iterează prin mașini.
● Când găsesti Lastun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 5', 20 * '-')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        masini_vechi.append(masina)
        index_masina = masini.index(masina)
        masini[index_masina] = 'Tesla'

print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')


"""
6. Având dict:
pret_masini = {'Dacia': 6800, 'Lăstun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}
Vine un client cu un buget de 15000 euro.
a) Iterează prin dict.items() și accesează mașina și prețul.
● Prezintă doar mașinile care se încadrează în acest buget.

b) Iterează prin listă.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 6', 20 * '-')

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

buget_client = 15000
masini_in_buget = []

print(5 * '-', 'a) Masina-Pret in buget', 5 * '-')
for masina, pret in pret_masini.items():
    if pret <= buget_client:
        print(f'Masina {masina} se incadreaza in bugetul dumneavoastra, pretul aferent este {pret}')

print(5 * '-', 'b) Masina in buget', 5 * '-')
for masina in pret_masini:
    if pret_masini.get(masina) < buget_client:
        print(f'Pentru un buget de sub 15000 euro puteți alege mașina {masina}')


"""7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 7', 20 * '-')

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0

for numar in numere:
    if numar == 3:
        count += 1
print(f'Lista de numere este: {numere}')
print(f'Numarul 3 apare de {count} ori')


"""8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 8', 20 * '-')

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0

for numar in numere:
    sum += numar

print(f'Suma numerelor este: {sum}')


"""9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 9', 20 * '-')

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max_number = numere[0]

for numar in numere:
    if numar > max_number:
        max_number = numar

print(f'Numarul maxim din lista este: {max_number}')


"""10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 10', 20 * '-')

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3, 10]
print(f'Lista inainte de modificare: {numere}')

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]

print(f'Lista noua dupa modificare: {numere}')
