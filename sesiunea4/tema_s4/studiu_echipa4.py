"""1. Alege un număr de la tastatură -> Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

-> Ex:3
1
22
333
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')

nr_input = int(input('Alege un nr: '))

for i in range(nr_input + 1):
    print(str(i) * i)



# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')
"""2.
tastatura_telefon = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[0]]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""

tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]

print(5 * '-', 'a)', 5 * '-')
for lst in tastatura_telefon:
    for number in lst:
        print(f'Cifra curenta este {number}')

print(5 * '-', 'b)', 5 * '-')

is_active = True

while is_active:
    user_input = int(input('Tasteaza o cifra: '))
    for lst in tastatura_telefon:
        for number in lst:
            if 0 < user_input <= 3:
                if number == user_input:
                    print(f'Ati apasat cifra {number}')
            elif 4 <= user_input <= 6:
                if number == user_input:
                    print(f'Ati apasat cifra {number}')
            elif 7 <= user_input <= 9:
                if number == user_input:
                    print(f'Ati apasat cifra {number}')
            else:
                if number == user_input:
                    print(f'Ati apasat cifra {number}')
                    print('Vom iesi din comanda.')
                    is_active = False