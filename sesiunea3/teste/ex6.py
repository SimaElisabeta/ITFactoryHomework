def list_as_pretty(my_list):
    pretty = ''
    for i in range(len(my_list)):
        pretty += my_list[i]
        if i < len(my_list) - 1:
            pretty += ', '
    return pretty

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

# varianta 1
print(f'Elevii cu nota de trecere sunt: {list(dict1.keys())}')

# varianta 2 (am creat o functie ca sa imi scrie codul frumos: list_as_pretty)
# elevi_list = list(dict1.keys())
print(f'Elevii cu nota de trecere sunt: {list_as_pretty(list(dict1.keys()))}')



# EXERCITIUL 9
"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""
# REZOLVARE:
# varianta 1
print(f"Ana a luat nota {dict1.get('Ana')}")
print(f"Gigel a luat nota {dict1.get('Gigel')}")
print(f"Dorel a luat nota {dict1.get('Dorel')}")

# varianta 2 (cu ajutor google)
for elev, nota in dict1.items():                # elev = key, nota = value. So my for will iterate through all the items in my dict accessing it with dict1.items()
    print(f'{elev} a luat nota {nota}')         # here it will print key-value pair for each item in my dict



# EXERCITIUL 10
"""
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
"""
# REZOLVARE:
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

# varianta 1
dict1.pop('Gigel')
dict1.setdefault("Ionică", 9)
print(f'Dupa modificarile facute, elevii actuali ai clasei sunt: {list(dict1.keys())}')
print(f'Dupa modificarile facute, elevii actuali ai clasei sunt: {list_as_pretty(list(dict1.keys()))}')


# varianta 2 (foloseste 3 inputs pentru a scoate un elev si a introduce altul nou la care sa ii atribui si o nota)
"""
remove_elev = input('Transfera pe cine nu mai doresti in clasa: ')

try:
    dict1.pop(remove_elev)
except KeyError:
    print(f'Nu poti transfera {remove_elev} din clasa deoarece nu exista')

add_elev = input('Scrie numele noului elev: ')
add_nota = int(input('Scrie nota elevului nou adaugat: '))

dict1.setdefault(add_elev, add_nota)
print(f'Dupa modificarile facute, elevii actuali ai clasei sunt: {list_as_pretty(list(dict1.keys()))}')
"""




