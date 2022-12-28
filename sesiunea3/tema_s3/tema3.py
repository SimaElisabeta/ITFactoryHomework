def list_as_pretty(my_list):
    pretty = ''
    for i in range(len(my_list)):
        pretty += my_list[i]
        if i < len(my_list) - 1:
            pretty += ', '
    return pretty
# (am creat o functie ca sa imi transforme lista intr-un print mai frumos)
# sugestie Sergiu: Daca doresti sa afisezi mai frumos liste si dictionare poti folosi functia pprint (from pprint import pprint)


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
print(20 * '-', 'EXERCITIUL 1', 20 * '-')

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f'Lista note muzicale: {note_muzicale}')
note_muzicale = note_muzicale[::-1]
print(f'Note muzicale inversate: {note_muzicale}')
note_muzicale.reverse()
print(f'Note muzicare reverse: {note_muzicale}')



# EXERCITIUL 2
"""2. De câte ori apare ‘do’?"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')

print(f"nota 'do' apare doar {note_muzicale.count('do')} data") if note_muzicale.count('do') == 1 else print(f"nota 'do' apare de: {note_muzicale.count('do')} ori")



# EXERCITIUL 3
"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 3', 20 * '-')

# varianta 1
list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_new = list_1 + list_2
print(f'Create new variable and concatenate the 2 lists with "+" operator => list_new = list_1 + list_2: {list_new}')

# varianta 2
list_1.extend(list_2)
print(f'Concatenate list_1 with list_2 using list.extend() method: {list_1}')



# EXERCITIUL 4
"""
4. 
● Sortează și afișează lista generată la exercițiul anterior.
● Scoate numărul 0 folosind o funcție.
● Afișaza iar lista.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 4', 20 * '-')

list_new.sort()
print(f'Sorted list: {list_new}')
list_new.remove(0)
print(f'New list printed without number 0: {list_new}')



# EXERCITIUL 5 + EXERCITIUL 6
"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
● Lista este goală.
● Lista nu este goală.

6. Folosește o funcție care să șteargă lista de la exercițiul 3.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 5+6', 20 * '-')

# varianta 1 - pentru exercitiul 5
print(f'Lista actuala: {list_new} nu este goală.') if list_new != [] else print('Lista actuala este goală.')

# varianta 2 - pentru exercitiul 6
while True:
    question = input('Doresti sa golesti lista de numere? (Y/N) ').upper()
    if question == 'Y':
        list_new.clear()
        print(f'Am golit lista conform dorintei tale.')
        break
    elif question == 'N':
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
print(20 * '-', 'EXERCITIUL 7', 20 * '-')

print('Lista nu este goală.') if list_new != [] else print('Lista este goală acum.')



# EXERCITIUL 8
""""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 8', 20 * '-')
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}

# varianta 1
print(f'Elevii cu nota de trecere sunt: {list(dict1.keys())}')

# varianta 2 (am creat o functie ca sa imi transforme lista intr-un print mai frumos: list_as_pretty)
# elevi_list = list(dict1.keys())
print(f'Elevii cu nota de trecere sunt: {list_as_pretty(list(dict1.keys()))}')



# EXERCITIUL 9
"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 9', 20 * '-')

# varianta 1
print(f"Ana a luat nota {dict1.get('Ana')}")
print(f"Gigel a luat nota {dict1.get('Gigel')}")
print(f"Dorel a luat nota {dict1.get('Dorel')}")

# varianta 2 - am vrut sa gasesc o varianta care sa nu fie atat de repetitiva, folosind for am ajuns la rezolvarea asta
for i in dict1.keys():
    print(f'{i} a luat nota {dict1.get(i)}')

# varianta 3 - dupa am cautat mai multe pe google si am gasit varianta asta, cea mai frumoasa!
for elev, nota in dict1.items():                # elev = key, nota = value. So my for will iterate through all the items in my dict accessing it with dict1.items()
    print(f'{elev} a luat nota {nota}')         # on this line it will print key-value pair for each item in my dict



# EXERCITIUL 10
"""
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 10', 20 * '-')

dict1.update({'Dorel': 6})
print(f"Dupa contestatie nota lui Dorel s-a marit la {dict1.get('Dorel')}")



# EXERCITIUL 11
"""
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 11', 20 * '-')

# varianta 1
dict1.pop('Gigel')
print('A plecat Gigel')
dict1.setdefault("Ionică", 9)
print('A venit Ionică')
print(f"Dupa modificarile facute, elevii actuali ai clasei sunt: {list_as_pretty(list(dict1.keys()))}")

# varianta 2 - inflorita (folosesc 3 inputs: 1->pentru a scoate un elev 2-3> pentru a introduce altul nou la care sa ii atribui si o nota)
remove_elev = input('Transfera pe cine nu mai doresti in clasa: ')

try:
    dict1.pop(remove_elev)
except KeyError:
    print(f'Nu poti transfera {remove_elev} din clasa deoarece nu exista')

add_elev = input('Scrie numele noului elev care s-a transferat in clasa: ')
add_nota = int(input('Atribuie o nota elevului nou adaugat: '))

dict1.setdefault(add_elev, add_nota)
print(f'Dupa modificarile facute, elevii actuali ai clasei sunt: {list_as_pretty(list(dict1.keys()))}')
