"""
1. Clasa Factură
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fără serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x număr y
Data: generează automat data de azi
Produs      | cantitate     | preț bucată   | Total
Telefon     | 7             | 700           | 49000
"""

# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')


class Factura:
    from datetime import date
    seria = 'ESB'
    today = date.today()

    def __init__(self, numar, produse):
        self.numar = numar
        self.produse = produse
        # self.nume_produs = nume_produs
        # self.cantitate = cantitate
        # self.pret_buc = pret_buc

    def genereaza_factura(self):
        detalii_factura = f'Factura seria: {self.seria}, număr: {self.numar} \n' \
                          f'Data (zi/lună/an): {self.today.day}/{self.today.month}/{self.today.year} \n' \
                          f'Produs    |   cantitate   |   preț bucată   | Total   \n'

        produse_factura = ''
        for produs in self.produse:
            produse_factura += f'{produs.nume_produs}     |       {produs.cantitate}       |      {produs.pret_buc}      | {produs.pret_buc * produs.cantitate} \n'

        return detalii_factura + produse_factura


class Produs:

    def __init__(self, nume_produs, cantitate, pret_buc):
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def __str__(self):
        return f'{self.nume_produs}'

    def __repr__(self):
        return str(self)

    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua

    def schimba_pretul(self, pret_nou_buc):
        self.pret_buc = pret_nou_buc

    def schimba_nume_produs(self, nume_nou_produs):
        self.nume_produs = nume_nou_produs


# class ProduseDB:
#     produse = {}
#
#
# produse = ProduseDB()

# produse_in_cos = [produs1, produs2]
# produse_in_cos.append(produs3)
lista_produse = [Produs('Casti', 1, 500.00), Produs('Tableta', 2, 1500.00)]

factura1 = Factura(2101, lista_produse)
# factura2 = Factura(102, 'Casti', 1, 200.00)
# factura1.schimba_cantitatea(7)
# factura1.schimba_pretul(700.00)
# factura1.schimba_nume_produs('Tableta')
#
# print(f'Cantitate schimbata: {factura1.cantitate}')
# print(f'Pret schimbat: {factura1.pret_buc}')
# print(f'Nume produs schimbat: {factura1.nume_produs} \n')

print(factura1.genereaza_factura())

# lst = [produs1, produs2]
# print(lst)
