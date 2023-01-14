# 2. Alegeti 2 clase din cele implementate la tema anterioara, si scrieti unit teste
# pentru toate metodele, folosind unittest.
from dataclasses import dataclass


@dataclass
class Employee:
    nume: str
    prenume: str
    salariu: float

    def descrie(self):
        return f'Nume: {self.nume}, Prenume: {self.prenume}, Salariu: {self.salariu}'

    def nume_complet(self):
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def review_salariu(self, procent):
        calc_procent = self.salariu * (procent * 0.01)
        self.salariu = self.salariu + int(calc_procent)


@dataclass
class ContBancar:
    iban: str
    titular_cont: str
    sold: float

    def afisare_sold(self):
        return f'Titularul {self.titular_cont} are în contul {self.iban}, suma de {self.sold:.2f} lei'

    def debitare_cont(self, suma):
        if suma > self.sold:
            print('Fonduri insuficiente!')
        else:
            self.sold -= suma
            print(f"Suma de: {suma:.2f} RON a fost debitata din cont")

    def creditare_cont(self, suma):
        self.sold = self.sold + suma
