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



# varianta 2
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



