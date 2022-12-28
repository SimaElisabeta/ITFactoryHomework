"""
1.Clasa Cerc
Atribute: rază, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""

# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')


class Cerc:
    from math import pi

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        return f'Culoarea: {self.culoare}, Raza: {self.raza}'

    def aria(self):
        return self.pi * self.raza ** 2

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return self.diametru() * self.pi


c1 = Cerc(5, 'albastru')
c2 = Cerc(10, 'verde')

print(f'Descriere cerc 1: {c1.descrie_cerc()}')
print(f'Descriere cerc 2: {c2.descrie_cerc()}')

print(f'Aria cerc 1: {c1.aria()}')
print(f'Aria cerc 2: {c2.aria()}')

print(f'Diametru cerc 1: {c1.diametru()}')
print(f'Diametru cerc 2: {c2.diametru()}')

print(f'Circumferinta cerc 1: {c1.circumferinta()}')
print(f'Circumferinta cerc 2: {c2.circumferinta()}')

"""
2. Clasa Dreptunghi
Atribute: lungime, lățime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va 
suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""

# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')


class Dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        return f'Lungime: {self.lungime}, Latime: {self.latime}, Culoare: {self.culoare}'

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return (self.lungime + self.latime) * 2

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


d1 = Dreptunghi(10, 15, 'portocaliu')
d2 = Dreptunghi(7, 17, 'galben')

print(f'Descriere dreptunghi 1: {d1.descrie()}')
print(f'Descriere dreptunghi 2: {d2.descrie()}')

print(f'Aria dreptunghi 1: {d1.aria()}')
print(f'Aria dreptunghi 2: {d2.aria()}')

print(f'Perimetrul dreptunghi 1: {d1.perimetrul()}')
print(f'Perimetrul dreptunghi 2: {d2.perimetrul()} \n')

d1.schimba_culoarea('rainbow')
print(f'Update descriere culoare d1: {d1.descrie()}')

"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pentru toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""

# REZOLVARE:
print(20 * '-', 'EXERCITIUL 3', 20 * '-')


class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        return f'Nume: {self.nume}, Prenume: {self.prenume}, Salariu: {self.salariu}'

    def nume_complet(self):
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu_lunar() * 12

    def marire_salariu(self, procent):
        calc_procent = self.salariu * (procent * 0.01)
        self.salariu = self.salariu + int(calc_procent)


angajat1 = Angajat('Popovici', 'Dumitru', 2500)
angajat2 = Angajat('Simion', 'Bianca', 5000)

print(f'Angajatul 1 descriere: {angajat1.descrie()}')
print(f'Angajatul 2 descriere: {angajat2.descrie()}')

print(f'Angajatul 1 nume complet: {angajat1.nume_complet()}')
print(f'Angajatul 2 nume complet: {angajat2.nume_complet()} \n')

print(f'Angajatul 1 salariu lunar: {angajat1.salariu_lunar()}')
print(f'Angajatul 2 salariu lunar: {angajat2.salariu_lunar()}')

print(f'Angajatul 1 salariu anual: {angajat1.salariu_anual()}')
print(f'Angajatul 2 salariu anual: {angajat2.salariu_anual()} \n')

angajat1.marire_salariu(100)
angajat2.marire_salariu(10)
print(f'Angajatul 1 salariu lunar dupa marire: {angajat1.salariu_lunar()}')
print(f'Angajatul 2 salariu lunar dupa marire: {angajat2.salariu_lunar()}')

"""
4. Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""

# REZOLVARE:
print(20 * '-', 'EXERCITIUL 4', 20 * '-')


class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return f'Titularul {self.titular_cont} are în contul {self.iban}, suma de {self.sold} lei'

    def debitare_cont(self, suma):
        self.sold = self.sold - suma

    def creditare_cont(self, suma):
        self.sold = self.sold + suma


titular1 = Cont('RO1854241300011RON', 'Popescu Florin', 1000.00)
titular2 = Cont('RO4488542236477RON', 'Mugur Alexandru', 2800.91)

print(titular1.afisare_sold())
print(titular2.afisare_sold())
print('')

titular1.debitare_cont(500)
titular2.debitare_cont(300.91)
print(f'Afisare cont dupa DEBITARE: {titular1.afisare_sold()}')
print(f'Afisare cont dupa DEBITARE: {titular2.afisare_sold()}')
print('')

titular1.creditare_cont(100)
titular2.creditare_cont(1000)
print(f'Afisare cont dupa CREDITARE: {titular1.afisare_sold()}')
print(f'Afisare cont dupa CREDITARE: {titular2.afisare_sold()}')
