# 8.Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}. Folositi o functie ca sa afisati Elevii (cheile)
print(20 * '-', 'EXERCITIUL 8', 20 * '-')

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

print(list(dict1.keys()))



# 9. Printati cei 3 elevi si notele lor.
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie.
print(20 * '-', 'EXERCITIUL 9', 20 * '-')

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#
# # v1 afisarea pentru un elev introdus de la tastatura
# student = input("Introduceti numele elevului pentru care vreti nota: ")
# print(f"{student} a luat nota {dict1[student]}")
#
# # v2 (afisarea notelor tuturor cu for pe care inca nu l`am invatat :D)
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# for key in dict1:
#     print(f"{key} a luat nota {dict1[key]}")
#
# # sau
# for elev, nota in dict1.items():
#     print(f'{elev} a luat nota {nota}')



# OPTIONAL
# 1. Ne imaginam o echipa de fotbal pt teren sintetic. 3 Schimbari maxime admise.
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3

# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’

# Testati codul cu diferite valori

# Google search hint
# “how to check if item is in list python”
print(20 * '-', 'OPTIONAL', 20 * '-')

playing = ["Leo", "Cristiano", "Erling", "Kylian", "Gianluigi"]
substitutes = ["Sergi", "Ferran", "Memphis", "Ansu", "Frenkie"]
substitutes_max = 3

substitutes_done = int(input("Introduceti cate schimbari au fost efectuate pana acum dintr-un maxim de 3: "))
player_to_change = input(f"Introduceti numele unui jucator pe care sa il schimbati dintre {playing}:")
if player_to_change in playing:
    if substitutes_done < substitutes_max:
        player_in = substitutes.pop()
        playing.remove(player_to_change)
        playing.append(player_in)
        substitutes_done += 1
        print(f"A intrat {player_in}, a iesit {player_to_change}, mai aveti {substitutes_max - substitutes_done} schimbari")
    print(f"Mai aveti {substitutes_max - substitutes_done} schimbari ")
else:
    print(f"Nu se poate efectua schimbarea, deoarece jucatorul {player_to_change} nu e in teren!")