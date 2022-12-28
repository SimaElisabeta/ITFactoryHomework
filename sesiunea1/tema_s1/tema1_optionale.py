# EXERCITIUL 1 - optional
# REZOLVARE:

user_imput = input(">")                     # >01234 or >012345
middle_character = (len(user_imput)) // 2   # impartirea "//" imi va retruna un int
# print(user_imput[middle_character])

# varinata sa imi afiseze mereu litera sau literele din mijloc
# verificand daca dimensiunea cuvantului este par sau impar
if len(user_imput) % 2 == 1:
    print(f'Middle character: {user_imput[middle_character]}')      # >01234
else:
    print(f'Middle characters: {user_imput[middle_character - 1 : middle_character + 1]}')      # >012345



# EXERCITIUL 2 - optional
# REZOLVARE:
# word_1, word_2 = input().split()
# print(word_1, word_2)






