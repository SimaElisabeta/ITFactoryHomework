"""
1. Funcție care primește o lună din an și returnează câte zile are acea lună.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')

def count_total_days_in_month(month, year):
    months = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }
    if year % 4 == 0 and month == 'February':
        return 29
    return months.get(month)

print(count_total_days_in_month('February', 2020), 'days')
print(count_total_days_in_month('February', 2023), 'days')

"""
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')

def calculator(nr1, nr2):
    assert nr2 > 0, 'Primul numar nu se poate imparti la 0'
    return [(nr1 + nr2), (nr1 - nr2), (nr1 * nr2), (nr1 // nr2)]

a, b, c, d = calculator(10, 5)

print("Suma:", a)
print("Diferenta:", b)
print("Inmultirea:", c)
print("Impartirea:", d)


"""
3. Funcție care primește o listă de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {0: 0, 1 :2, 2: 0, 3: 1, 4: 0, 5: 3, 6: 0, 7: 2, 8: 0, 9: 1}
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 3', 20 * '-')

def numbers_count(lst):
    dict = {}
    for i in range(10):
        dict.setdefault(i, 0)
    for key in dict.keys():
        if key in lst:
            count = lst.count(key)
            dict[key] = count
    return dict

print(numbers_count([1, 3, 1, 5, 9, 7, 7, 5, 5]))


"""
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 4', 20 * '-')

# v1
def get_max_v1(nr1, nr2, nr3):
    lst = [nr1, nr2, nr3]
    maxim = lst[0]
    for number in lst:
        if number > maxim:
            maxim = number
    return maxim

print(get_max_v1(5, 10, 2))

# v2 - uses max function
def get_max_v2(nr1, nr2, nr3):
    lst = [nr1, nr2, nr3]
    return max(lst)

print(get_max_v2(55, 10, 2))

# v3 - uses max function and gets a collection of arguments (*numbers) as parameter
def get_max_v3(*numbers):
    lst = [*numbers]
    return max(lst)

print(get_max_v3(55, 10, 20, 66, 15, 7, 0))


"""
5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 5', 20 * '-')

# v1
def sum_of_nr(number):
    the_sum = 0
    for i in range(number + 1):
        the_sum += i
    return the_sum

print(sum_of_nr(3))
print(sum_of_nr(10))
