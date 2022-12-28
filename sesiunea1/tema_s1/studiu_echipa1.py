# EXERCITIUL 1 - studiu in echipa
# REZOLVARE:
word = input('Scrie un cuvant: ')
first_char = word[0]
last_char = word[-1]
char_replacing = word[1:-1].replace(f'{first_char}', f'{first_char.upper()}')
word = first_char + char_replacing + last_char

print(word)


# EXERCITIUL 2 - studiu in echipa
# REZOLVARE:

user = input('user> ')
password = input('password> ')
hidden_password = '*' * len(password)

print(f'Parola pt user {user} este {hidden_password} si are {len(password)} caractere')





