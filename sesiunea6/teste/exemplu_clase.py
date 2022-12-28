class Persoana:

    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.haine = []

    def __str__(self):
        return f'nume:{self.nume}, prenume:{self.prenume}, varsta: {self.varsta}, haine: <{self.haine}>'

    def __repr__(self):
        return str(self)


class Haina:

    def __init__(self, nume, culoare):
        self.nume = nume
        self.culoare = culoare

    def __str__(self):
        return f'nume:{self.nume}, culoare:{self.culoare}'

    def __repr__(self):
        return str(self)


# pers1 = Persoana('Goia', 'Ghita', 31)
# pers2 = Persoana('Popa', 'Dana', 78)
# pers3 = Persoana('Mihail', 'Costel', 18)

# lst = [pers1, pers2, pers3]
# print(lst)

lst = []
lst_adulti = []
nr = int(input('Introduceti nr de persoane: '))

for i in range(nr):
    print(f'Persoana nr {i+1}')
    nume = input('Nume: ')
    prenume = input('Prenume: ')
    varsta = int(input('Varsta: '))
    persoana = Persoana(nume, prenume, varsta)
    nr_haine = int(input('Nr de haine: '))
    for j in range(nr_haine):
        nume_haina = input('Haina de tip: ')
        culoare_haina = input('Culoare haina: ')
        haina = Haina(nume_haina, culoare_haina)
        persoana.haine.append(haina)
    lst.append(persoana)

for i in lst:
    print(i)

#
# for persoana in lst:
#     if persoana.varsta > 18:
#         print(persoana.nume)
#         lst_adulti.append(persoana)
#
# print(lst_adulti)
