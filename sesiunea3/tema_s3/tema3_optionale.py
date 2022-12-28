def list_as_pretty(my_list):
    pretty = ''
    for i in range(len(my_list)):
        pretty += my_list[i]
        if i < len(my_list) - 1:
            pretty += ', '
    return pretty
# (am creat o functie ca sa imi transforme lista intr-un print mai frumos: list_as_pretty)
# sugestie Sergiu: Daca doresti sa afisezi mai frumos liste si dictionare poti folosi functia pprint (from pprint import pprint)

# EXERCITIUL 1
"""
1. Ne imaginăm o echipă de fotbal pt teren sintetic. 3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
- Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
"""

jucatori_pe_teren = ['Hagi', 'Popescu', 'Petrescu', 'Mutu', 'Chivu']
schimbari_max = 3
schimbari_efectuate = 0
print(f'Jucatorii disponibili pe teren sunt: {list_as_pretty(jucatori_pe_teren)}.')


contiuna_schimbarea = True

while contiuna_schimbarea:
    if schimbari_efectuate < schimbari_max:
        jucator_iesit = input('Pe cine doresti sa scoti din teren? ')

        if jucator_iesit in jucatori_pe_teren:
            schimbari_efectuate += 1
            jucator_intrat = input(f'Pe cine doresti sa introduci pe teren in locul lui {jucator_iesit}? ')
            jucatori_pe_teren.remove(jucator_iesit)
            jucatori_pe_teren.append(jucator_intrat)
            print(
                f'A intrat {jucator_intrat}, a ieșit {jucator_iesit}, mai ai {schimbari_max - schimbari_efectuate} schimbări disponibile.')
            while True:
                intrebare = input('Doresti sa continui cu schimbarile? (Y/N) ').upper()
                if intrebare == 'Y':
                    # contiuna_schimbarea = True
                    break
                elif intrebare == 'N':
                    contiuna_schimbarea = False
                    break
                else:
                    print('Nu ai introdus un raspuns valid, mai incearca.')
        else:
            print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren.')
            print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbări disponibile.')
    else:
        print('Imi pare rau, nu poti continua. Ai atins limita de schimbari posibile.')
        contiuna_schimbarea = False
else:
    print(f'Jucatorii actuali pe teren sunt: {list_as_pretty(jucatori_pe_teren)}.')