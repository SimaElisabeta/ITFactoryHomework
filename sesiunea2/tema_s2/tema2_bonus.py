import random

# EXERCITIUL 1
"""
Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
"""
# REZOLVARE:
user_guess = int(input('Alege un numar de la 1 la 10: '))
dice_roll = random.randint(1, 10)

if user_guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {user_guess} dar a fost {dice_roll}.')
elif user_guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {user_guess} dar a fost {dice_roll}.')
elif user_guess == dice_roll:
    print(f'Ai ghicit. Felicitări! Ai ales {user_guess} si zarul a fost {dice_roll}.')


