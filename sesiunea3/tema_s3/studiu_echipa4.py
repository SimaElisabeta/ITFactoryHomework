from pprint import pprint


# . EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ .
# 1. Set
print(20 * '-', 'EXERCITIUL 1', 20 * '-')

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișează zile_sapt

zile_sapt.add('luni')
print(zile_sapt)

# 2.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
print(20 * '-', 'EXERCITIUL 2', 20 * '-')

if  weekend.issubset(zile_sapt) == True:
    print('Weekend este un subset al zilelor din săptămânii')
else:
    print('Weekend nu este un subset al zilelor din săptămânii')

# 3. Afișează diferențele dintre aceste 2 seturi.
print(zile_sapt-weekend)

# 4. Afișează intersecția elementelor din aceste 2 seturi.
print(zile_sapt & weekend)