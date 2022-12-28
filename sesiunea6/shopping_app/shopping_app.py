# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')


class Factura:
    from datetime import date
    seria = 'ESB'
    today = date.today()

    def __init__(self, numar, produse):
        self.numar = numar
        self.produse = produse  # lista de produse

    def genereaza_factura(self):
        detalii_factura = f'Factura seria: {self.seria}, număr: {self.numar} \n' \
                          f'Data (zi/lună/an): {self.today.day}/{self.today.month}/{self.today.year}\n' \
                          f"{'Produs':<15}| {'cantitate':<15}| {'preț bucată':<15}| {'Total'}\n"

        produse_factura = ''
        for produs in self.produse:
            produse_factura += f"{produs.nume_produs:<15}| {produs.cantitate:<15}| {produs.pret_buc:<15}| {produs.pret_buc * produs.cantitate}\n"

        return detalii_factura + produse_factura


class Produs:
    cantitate = 1

    def __init__(self, nume_produs, pret_buc):
        self.nume_produs = nume_produs
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


class ProduseDB:
    produse = [
        Produs(nume_produs='Telefon', pret_buc=150.00),
        Produs(nume_produs='Tableta', pret_buc=1000.00),
        Produs(nume_produs='Casti', pret_buc=100.00),
        Produs(nume_produs='Gorilla glass', pret_buc=200.00)
    ]

    def __str__(self):
        return f'{self.produse}'

    def __repr__(self):
        return str(self)

    def cauta_produs(self, produs):
        for produs_object in self.produse:
            if produs_object.nume_produs == produs:
                return produs_object


db = ProduseDB()
produse_in_cos = []


def incearca_adauga_produs(nume_produs, cantitatea):
    rezultat = db.cauta_produs(nume_produs)
    if rezultat is not None:
        produse_in_cos.append(rezultat)
        rezultat.schimba_cantitatea(cantitatea)

def goleste_cos():
    produse_in_cos.clear()


incearca_adauga_produs('Telefon', 2)
incearca_adauga_produs('Casti', 3)
incearca_adauga_produs('Gorilla glass', 1)
incearca_adauga_produs('Casti HiFi', 1)


factura1 = Factura(2101, produse_in_cos)
print(factura1.genereaza_factura())