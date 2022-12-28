# EXERCITIUL 1
"""
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
"""
# REZOLVARE:

# if else functioneaza pe principiul unor ramuri bazata pe o conditie Adevarata sau Falsa.
# cu ajutorul if (elif) else poti dirija ramura pe care doresti ca aplicatia sa intre.
# astfel, in if else programul evalueaza o conditie
# daca aceasta este adevarata atunci programul intra pe ramura ei si va rula tot ce se afla in zona aceea
# daca programul nu este satisfacut de nici o conditie (primese ca raspuns doar valaoarea False)
# atunci va sari peste toate linile de cod si va rula tot ce se afla in zona 'else'



# EXERCITIUL 2
"""
2. Verifică și afișează dacă x este număr natural sau nu.
"""
# REZOLVARE:
x = 0

if isinstance(x, int) and (x > 0):          # !!! nr natural trebuie sa fie mai mare ca 0!
    print(f'{x} este un numar natural')     # nr natural (int): 15
else:
    print(f'{x} este un numar real')        # nr real (float): 15.0



# EXERCITIUL 3
"""
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
"""
# REZOLVARE:
x = 100

if x > 0:
    print(f'{x} este un numar pozitiv')
elif x < 0:
    print(f'{x} este un numar negativ')
else:
    print(f'{x} este un numar neutru')



# EXERCITIUL 4
"""
4. Verifică și afișează dacă x este între -2 și 13.
"""
# REZOLVARE:
x = 14

# variana 1
if (x >= -2) and (x <= 13):
    print(f'Numarul {x} se afla intre -2 si 13')

# varianta 2
if x in range(-2, 14):
    print(f'Numarul {x} se afla intre -2 si 13')



# EXERCITIUL 5
"""
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
"""
# REZOLVARE:
x = -10
y = -6

if x-y < 5:
    print(f'Diferenta ditre {x} si {y} este mai mica ca 5')
    print(f'Diferenta ditre {x} si {y} este de {x-y}')



# EXERCITIUL 6
"""
6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
"""
# REZOLVARE:
x = 28

# varianta 1
if x not in range(5, 28):
    print(f'{x} nu se afla intre 5 si 27')

# varianta 2 (data de Sergiu)
if not 5 <= x <=27:
    print(f'{x} nu se afla intre 5 si 27')



# EXERCITIUL 7
"""
7. x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
"""
# REZOLVARE:
x = 88
y = 88

if x == y:
    print(f'{x} este egal cu {y}')
else:
    if x > y:
        print(f'x->{x} este mai mare ca y->{y}')
    if y > x:
        print(f'y->{y} este mai mare ca x->{x}')



# EXERCITIUL 8
"""
8. X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
"""
# REZOLVARE:
x, y, z = 10, 1, 10

echilateral = (x == y == z)
isoscel = (x == y and x != z) or (y == z and y != x) or (x == z and y != x)
oarecare = x != y and x != z and y != z

if echilateral:
    print(f'Triunghiul este ECHILATERAL')
elif isoscel:
    print(f'Triunghiul este ISOSCEL')
elif oarecare:
    print(f'Triunghiul este OARECARE')



# EXERCITIUL 9
"""
9. Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu.
"""
# REZOLVARE:
char = input('Scrie un singur caracter pentru a primi raspunsul daca este vocala sau nu: ').lower()
vocale = 'aeiouăâî'

# varianta 1
if 'a' in char:
    print('caracterul este o vocala')
elif 'e' in char:
    print('caracterul este o vocala')
elif 'i' in char:
    print('caracterul este o vocala')
elif 'o' in char:
    print('caracterul este o vocala')
elif 'u' in char:
    print('caracterul este o vocala')
elif 'ă' in char:
    print('caracterul este o vocala')
elif 'â' in char:
    print('caracterul este o vocala')
elif 'î' in char:
    print('caracterul este o vocala')
else:
    print('caracterul este o consoana')


# varianta 2
if char in vocale:
    print('caracterul este o vocala')
else:
    print('caracterul este o consoana')



# EXERCITIUL 10
"""
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""
# REZOLVARE:
nota = int(input('Da o nota de la 1 la 10: '))

if nota > 9:
    print('Nota echivalenta in sistemul american este: A')
elif nota > 8:
    print('Nota echivalenta in sistemul american este: B')
elif nota > 7:
    print('Nota echivalenta in sistemul american este: C')
elif nota > 6:
    print('Nota echivalenta in sistemul american este: D')
elif nota > 4:
    print('Nota echivalenta in sistemul american este: E')
elif nota <= 4:
    print('Nota echivalenta in sistemul american este: F')








