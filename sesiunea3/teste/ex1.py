# EXERCITIUL 1
"""
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o.
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
"""
# REZOLVARE:

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)



# EXERCITIUL 2
"""2. De câte ori apare ‘do’?"""
# REZOLVARE:

print(f"nota 'do' apare doar {note_muzicale.count('do')} data") if note_muzicale.count('do') == 1 else print(f"nota 'do' apare de: {note_muzicale.count('do')} ori")



# EXERCITIUL 3
"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
"""
# REZOLVARE:
# varianta 1
list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_new = list_1 + list_2
print(f'Create new variable and concatenate the 2 lists with "+" operator => list = list_1 + list_2: {list_new}')
# varianta 2
list_1.extend(list_2)
print(f'Concatenate list 1 with list.extend() method: {list_1}')



# EXERCITIUL 4
"""
4. 
● Sortează și afișează lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
"""
# REZOLVARE:
list_new.sort()
print(f'Sorted list: {list_new}')



# EXERCITIUL 5 + EXERCITIUL 6
"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
● Lista este goală.
● Lista nu este goală.

6. Folosește o funcție care să șteargă lista de la exercițiul 3.
"""
# REZOLVARE:
# varianta 1 - pentru exercitiul 5
print('Lista actuala nu este goală.') if list_new != [] else print('Lista actuala este goală.')

# varianta 2 - pentru exercitiul 6
while True:
    question = input('Doresti sa golesti lista de numere? (Y/N) ').lower()
    if question == 'y':
        list_new.clear()
        print(f'Am golit lista conform dorintei tale.')
        break
    elif question == 'n':
        print(f'Lista a ramas neschimbata.')
        break
    else:
        print('Nu ai introdus un raspuns valid, mai incearca.')



# EXERCITIUL 7
"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
"""
# REZOLVARE:
print('Lista nu este goală.') if list_new != [] else print('Lista este goală acum.')



# EXERCITIUL 8
""""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""
# REZOLVARE:
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}






