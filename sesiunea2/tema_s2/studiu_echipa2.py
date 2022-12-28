# EXERCITIUL 1
"""
1. Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
"""

# my_string = input('Scrie ceva: ').lower()

# assert my_string[0] == my_string[len(my_string)-1], f'Prima litera si ultima litera nu sunt asemanatoare!'

# EXERCITIUL 2
"""
2. Având stringul '0123456789'
● Afișează doar numerele pare
● Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
"""
# varianta 1
string_numbers = '0123456789'

numere_pare = string_numbers[:-1:2]
numere_impare = string_numbers[1::2]
print(f'Numere pare: {numere_pare}')
print(f'Numere impare: {numere_impare}')



# varianta 2
cifre_string = input('Scrie un sir de numere: ')
cifre_lista = list(cifre_string)

cifre_pare = ''
cifre_impare = ''

for i in cifre_lista:
    i = int(i)
    if i % 2 == 0:
        i = str(i)
        cifre_pare += i

    else:
        i = str(i)
        cifre_impare += i

print(f'Cifre pare: {cifre_pare}')
print(f'Cifre impare: {cifre_impare}')



# varianta 3
#
# cifre_string = input('Scrie un sir de numere: ')
# lista_string = list(map(int, cifre_string))
#
# lista_pare = []
# lista_impare = []
# for i in lista_string:
#     if i % 2 == 0:
#         lista_pare.append(i)
#     else:
#         lista_impare.append(i)
#
# print(lista_pare)
# print(lista_impare)




