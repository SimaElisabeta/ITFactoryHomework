# EXERCITIUL 1
# REZOLVARE:
# variabila este zona din memoria unui calculator care tine date


# EXERCITIUL 2
# REZOLVARE:
book_name = 'Vanatorii de zmei'             # string
in_stock = 1000                             # int
book_price = 29.49                          # float
is_available = True                         # bool


# EXERCITIUL 3
# REZOLVARE:

print(type(book_name))
print(type(in_stock))
print(type(book_price))
print(type(is_available))


# EXERCITIUL 4
# REZOLVARE:
book_price = round(book_price)
print(f'{book_price}$ {type(book_price)}')


# EXERCITIUL 5
# REZOLVARE:
print(f'Your selected book is: {book_name}')
print(f'Check for availability: {is_available}')
print(f'Available books in our stock: {in_stock} pcs')
print(f"The selected book it's at the great price of just: {book_price}$")


# EXERCITIUL 6
# REZOLVARE:
# first_name = input('Nume: ')
# last_name = input('Prenume: ')
# total_car = len(first_name) + len(last_name)
#
# print(f'Numele tau este: {first_name} {last_name}')
# print(f'Numele complet are {total_car} caractere')


# EXERCITIUL 7
# REZOLVARE:
# L = int(input('lungimea = '))
# l = int(input('latimea = '))
# arie_dreptunghi = L * l
# print(f'Aria dreptunghiului este: {arie_dreptunghi}')


# EXERCITIUL 8
# REZOLVARE:
prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.count('the'))                   # counts how many times 'the' as characters appear in my string
prop_as_list = prop.split()                # it will split my string / sentence, and will convert the string into a list
print(type(prop_as_list))
print(f"Final answer: {prop_as_list.count('the')} times")       # counts how many times the word 'the' appear in my list

# EXERCITIUL 9
# REZOLVARE:
print(prop.replace('the', 'THE'))


# EXERCITIUL 10
# REZOLVARE:
# * assert verifies if the statement (assert - afirmarea) is True or False
# * if assert is True the code will continue to the next line code
# * if assert is False, then an error will appear and the code will not continue to the next line
assert prop.isnumeric() # here assert is False => function: prop.isnumeric() returns a False statement










