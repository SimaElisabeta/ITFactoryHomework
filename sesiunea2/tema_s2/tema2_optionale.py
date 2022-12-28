# EXERCITIUL 1
"""
1. Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""
# REZOLVARE:
x = int(input('Scrie un numar cu mai multe cifre: '))

# varianta 1
if len(str(x)) >= 4:
    print(f'x = {x}, x are minim 4 cifre ')
else:
    print(f'x = {x}, x are mai putin de 4 cifre')
    print('0 nu se considera ca fiind cifra')

# varianta 2
if x >= 1000 or x <= -1000:
    print(f'x = {x}, x are minim 4 cifre ')
else:
    print(f'x = {x}, x are mai putin de 4 cifre')
    print('0 nu se considera ca fiind cifra')



# EXERCITIUL 2
"""
2. Verifică dacă x are exact 6 cifre.
"""
# REZOLVARE:
x = int(input('Scrie un numar cu mai multe cifre: '))

# varianta 1
if len(str(x)) == 6:
    print('Sirul de cifre date are exact 6 caractere')
else:
    print('0 nu se considera ca fiind cifra')

# varianta 2
if ((x >= 100000) and (x <= 999999)) or ((x >= -100000) and (x <= -999999)):
    print('Sirul de cifre date are exact 6 caractere')
else:
    print('0 nu se considera ca fiind cifra')



# EXERCITIUL 3
"""
3. Verifică dacă x este număr par sau impar (x e int).
"""
# REZOLVARE:
x = 10

if x % 2 == 0:
    print(f'x ({x}) este numar par')
else:
    print(f'x ({x}) este numar impar')



# EXERCITIUL 4
"""
4. x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""
# REZOLVARE:
x, y, z = 7, 10, 1

if (x > y) and (x > z):
    print('x este cel mai mare dintre numere')
elif (y > x) and (y > z):
    print('y este cel mai mare dintre numere')
elif (z > x) and (z > y):
    print('z este cel mai mare dintre numere')
else:
    print('2 numere se repeta, nu s-a putut determina numarul maxim')
    # va intra in else daca spre exemplu: x=7, y=7, z=6
    # adica daca cifra cea mai mare se repeta de 2 ori, programul nu va reusi sa determine care e numarul cel mai mare



# EXERCITIUL 5
"""
5. X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
"""
# REZOLVARE:
x, y, z = 60, 60, 60

if x + y + z == 180:
    print('triunghiul este valid')
else:
    print('triunghiul nu este valid')



# EXERCITIUL 6
"""
6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citește de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
# REZOLVARE:
prop = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Scrie te rog o cifra: '))
new_prop = prop[:-x]
print(new_prop)



# EXERCITIUL 7
"""
7. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
"""
# REZOLVARE:
prop = 'Coral is either the stupidest animal or the smartest rock'
first_5_char = prop[:5]
last_5_char = prop[-5:]
new_prop = first_5_char + last_5_char
print(new_prop)



# EXERCITIUL 8
"""
8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvânt
● output: 'Coral is either the stupidest animal or the smartest'
"""
# REZOLVARE:
prop = 'Coral is either the stupidest animal or the smartest rock'
rock_start_index = prop.index('rock')
new_prop = prop[:rock_start_index]
print(new_prop)
