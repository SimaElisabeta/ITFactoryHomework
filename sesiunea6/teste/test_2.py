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
    seria = 'FDB'
    today = date.today()

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
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

    def genereaza_factura(self):
        return f'Factura seria: {self.seria}, număr: {self.numar} \n' \
               f'Data (zi/lună/an): {self.today.day}/{self.today.month}/{self.today.year} \n' \
               f'Produs  | cantitate | preț bucată | Total \n' \
               f'{self.nume_produs} | {self.cantitate}         | {self.pret_buc}       | {self.pret_buc * self.cantitate}'


factura1 = Factura(2201, 'Telefon', 1, 500.00)

factura1.schimba_cantitatea(7)
factura1.schimba_pretul(700.00)
factura1.schimba_nume_produs('Nokia S')

print(factura1.genereaza_factura())
print('')

factura2 = Factura(2202, 'Casti', 1, 200.00)
factura2.schimba_cantitatea(3)
factura2.schimba_pretul(150.00)
factura2.schimba_nume_produs('Casti HiFi')
print(factura2.genereaza_factura())

"""
2. Clasa Mașină
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori
disponibile (set), înmatriculată (bool)
Culoare = gri - toate mașinile când ies din fabrică sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
Culori disponibile = alege tu 5-7 culori
Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e
negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""

# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')


class SpeedCannotBeLowerException(Exception):
    pass


class ColorNotInRangeException(Exception):
    pass


class Masina:
    marca = 'Citroen'
    viteza_actuala = 0
    culoare = 'Gri'
    culori_disponibile = ('Negru', 'Alb', 'Rosu', 'Verde', 'Albastru')
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        return f'Marca: {self.marca} \n' \
               f'Viteza actuala: {self.viteza_actuala} \n' \
               f'Culoare: {self.culoare} \n' \
               f'Inmatriculata: {self.inmatriculata} \n' \
               f'Model: {self.model} \n' \
               f'Viteza maxima: {self.viteza_maxima}'

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            raise Exception(f'Nu avem aceasta culoare,'
                            f'Culorile disponibile sunt: {self.culori_disponibile}')

    def accelereaza(self, viteza):
        if viteza < 0:
            raise SpeedCannotBeLowerException('Viteza de accelerare nu poate fi mai mica ca 0')
        if viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        self.viteza_actuala = 0


masina1 = Masina('C4 Sport', 250)
masina1.inmatriculare()
masina1.vopseste('Negru')
masina1.accelereaza(150)
masina1.franeaza()

print(masina1.descrie())

