# 1. Functie care sa calculeze si sa returneze suma a 2 numere
def suma(a, b):
    return a + b


# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def is_even(nr):
    return nr % 2 == 0


print(is_even(8))


# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
def name_length(last, middle, first):
    return len(last + middle + first)


print(name_length("Badea", "Gheorghe", "Ioan"))


# 4. Functie care returneaza aria dreptunghiului

def rectangle_area(length, width):
    return length * width


# 5. Functie care returneaza aria cercului
from math import pi


def circle_area(radius):
    return pi * radius ** 2


# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
def is_char_in_str(x, string):
    return x in string


print(is_char_in_str('a', 'My test string'))


# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
def lower_upper_count(string):
    upper_lower = {'upper': 0, 'lower': 0}
    for c in string:
        if c.isupper():
            upper_lower['upper'] += 1
        elif c.islower():
            upper_lower['lower'] += 1

    return upper_lower


print(lower_upper_count("Hello World!"))


# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
def list_of_positives(lst):
    res_list = []
    for n in lst:
        if n > 0:
            res_list.append(n)

    return res_list


print(list_of_positives([1, -6, -4, 22, 5, 3, -9]))


# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.
def get_biggest(x, y):
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea nr {y}")
    elif x < y:
        print(f"Al doilea numar {y} este mai mare decat primul nr {x}")
    else:
        print("Numerele sunt egale")


# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
def add_to_set(n, numbers_set):
    if n in numbers_set:
        print('Nu am adaugat numarul in set. Acesta exista deja')
        return False
    else:
        numbers_set.add(n)
        print('Am adaugat numarul in set')
        return True


print(add_to_set(3, {1, 2, 4, 5}))

# OPTIONALE
# 1. Functie care primeste o luna din an si returneaza cate zile are acea luna
from calendar import monthrange
from datetime import datetime


def month_days_number(month):
    year = datetime.today().year
    return monthrange(year, month)[1]


print(month_days_number(9))


# 2. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere

# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
def calculator(x, y):
    return x + y, x - y, x * y, x / y


a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


# 3. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare cifra
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

# v1
def digits_count_v1(digits):
    dct = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for d in digits:
        dct[d] += 1

    return dct


print(digits_count_v1([1, 3, 1, 5, 9, 7, 7, 5, 5]))


# v2
def digits_count_v2(digits):
    dct = {}
    for d in digits:
        if d in dct:
            dct[d] += 1
        else:
            dct[d] = 1
    return dct


print(digits_count_v2([1, 3, 1, 5, 9, 7, 7, 5, 5]))


# 4. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele
def maximum(x, y, z):
    return max(x, y, z)


print(maximum(5, 3, 7))


# 5. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)
def sum_til_nr(nr):
    s = 0
    for x in range(nr + 1):
        s += x
    return s


print(sum_til_nr(3))


# # BONUS
# 1. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune

# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}
def common_numbers(lst1, lst2):
    return set(lst1) & set(lst2)


print(common_numbers([1, 1, 2, 3], [2, 2, 3, 4]))


# 2. Functie care sa aplice o reducere de pret. Daca apelul functiei nu primeste valoarea reducerii, sa ia valoarea default 10%.
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
def discount(price, discount_percent=10):
    if 0 <= discount_percent <= 100:
        return price - price * discount_percent / 100
    print("Reducerea aplicata nu este valida")


print(discount(100, 50))
print(discount(100))



# STUDIU IN ECHIPA
# 1. Functie care sa afiseze data si ora curenta din ro
# (bonus: afisati si data si ora curenta din China)
from datetime import datetime, timedelta, timezone


# v1
def display_date_time_v1():
    now = datetime.now()
    print(f"Date and time Romania: {now}")
    print(f"Date and time China: {now + timedelta(hours=5)}")


display_date_time_v1()

# v2
import pytz


def display_date_time_v2():
    timezone_ro = pytz.timezone(
        'Europe/Bucharest')  # pt v2, trebuie stiute timezone-uri sau aflate (print(pytz.all_timezones))
    now = datetime.now(timezone_ro)
    print(f"Date and time Romania: {now}")

    timezone_cn = pytz.timezone('Asia/Hong_Kong')
    now = datetime.now(timezone_cn)
    print(f"Date and time China: {now}")


display_date_time_v2()

# 2. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
from datetime import datetime


def days_til_birthday(birthday_date="25.12.2022"):
    birthday_date = datetime.strptime(birthday_date, "%d.%m.%Y")
    today = datetime.today()

    days_left = (birthday_date - today).days
    print(days_left)


days_til_birthday()