import math

"""
1. Funcție care să calculeze și să returneze suma a două numere
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')

def get_sum(a, b):
    return a + b

print(f'1. Suma numerelor este: {get_sum(10,1)}')
print(f'2. Suma numerelor este: {get_sum(10,7)}')


"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')

def is_even(number):
    if number % 2 == 0:
        return True
    return False

# number_input = int(input("Let's find if the number is odd or even: \n"))
number_input = 10

print('Your number is even.') if is_even(number_input) else print('Your number is odd.')


"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 3', 20 * '-')

def get_char_name_count(nume, prenume, nume_mijlociu):
    return len(nume + prenume + nume_mijlociu)

print(f"Nr total de caractere din numele complet este: {get_char_name_count('Sima', 'Elisabeta', '')}")


"""
4. Funcție care returnează aria dreptunghiului
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 4', 20 * '-')

def get_area_of_rectangle(L, l):
    return L * l

print(f'1. Aria dreptunghiului este: {get_area_of_rectangle(10, 50)}')
print(f'2. Aria dreptunghiului 2 este: {get_area_of_rectangle(20, 5)}')


"""
5. Funcție care returnează aria cercului
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 5', 20 * '-')

def get_area_of_circle(R):
    return math.pi * (R**2)

print(f'Aria cercului este: {get_area_of_circle(4)}')


"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 6', 20 * '-')

def check_char_in_str(txt, char):
    return char in txt

# the_string = input('Write something: \n')
# the_char = input('What character you want to check, to see if it exists in your string? \n')
the_string = 'Ana are mere'
the_char = 'a'

print(f'We found your character in string.') if check_char_in_str(the_string, the_char) else print("We couldn't find your character in the string")


"""
7. Funcție fără return, primește un string și printează pe ecran:
● Numărul de caractere lower case este x
● Numărul de caractere upper case exte y
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 7', 20 * '-')

def count_lower_upper_char(txt):
    lower_count = 0
    upper_count = 0
    for char in txt:
        if char.islower():
            lower_count += 1
        if char.isupper():
            upper_count += 1
    print(txt)
    print(f'Numărul de caractere lower case este: {lower_count}')
    print(f'Numărul de caractere upper case este: {upper_count}')

count_lower_upper_char('Ana are merE')
count_lower_upper_char('ANA are MERE')


"""
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 8', 20 * '-')

def get_positive_numbers(lst):
    new_list = []
    for nr in lst:
        if nr > 0:
            new_list.append(nr)
    return new_list

print(get_positive_numbers([10, 31, -1, 0, 5, -4, 7, 11, -25]))


"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ:
● Primul număr x este mai mare decat al doilea număr y
● Al doilea număr y este mai mare decat primul număr x
● Numerele sunt egale.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 9', 20 * '-')

def compare_numbers(nr1, nr2):
    if nr1 > nr2:
        print(f'Primul număr->{nr1} este mai mare decat al doilea număr->{nr2}')
    elif nr2 > nr1:
        print(f'Al doilea număr->{nr2} este mai mare decat primul număr->{nr1}')
    else:
        print(f'Numerele sunt egale')

print('1.')
compare_numbers(5, 10)
compare_numbers(50, 10)
compare_numbers(10, 10)
print('2.')
compare_numbers(0, 15)
compare_numbers(6, 5)
compare_numbers(1, 1)


"""
10. Funcție care primește un număr și un set de numere.
● Printează ‘am adaugat numărul nou în set’ + returnează True
● Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 10', 20 * '-')

def unique_numbers(nr, my_set):
    if nr not in my_set:
        my_set.add(nr)
        print(f'Am adaugat numărul nou în set')
        return True
    print('Nu am adaugat numărul în set. Acesta există deja')
    return False

print('True') if unique_numbers(9, {8, 10, 5, 1, 0}) else print('False')
print('True') if unique_numbers(1, {8, 10, 5, 1, 0}) else print('False')
