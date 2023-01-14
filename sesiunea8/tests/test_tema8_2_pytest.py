import pytest
from sesiunea8.app.tema8_2 import Employee, ContBancar


class TestTema8_2_Angajat:
    def setup_method(self):
        self.employee = Employee('Popovici', 'Dumitru', 3000)

    def test_descrie(self):
        assert self.employee.descrie() == 'Nume: Popovici, Prenume: Dumitru, Salariu: 3000'

    def test_nume_complet(self):
        assert self.employee.nume_complet() == 'Popovici Dumitru'

    def test_salariu_lunar(self):
        assert self.employee.salariu_lunar() == 3000

    def test_salariu_anual(self):
        assert self.employee.salariu_anual() == 36000

    @pytest.mark.parametrize('procent, expected', [
        (100, 6000),
        (0, 3000),
        (-50, 1500)
    ])
    def test_review_salariu(self, procent, expected):
        self.employee.review_salariu(procent)
        assert self.employee.salariu == expected


class TestTema8_2_ContBancar:
    def setup_method(self):
        self.titular = ContBancar('RO1854241300011RON', 'Popescu Florin', 1000.00)

    def test_afisare_sold(self):
        assert self.titular.afisare_sold() == 'Titularul Popescu Florin are în contul RO1854241300011RON, suma de 1000.00 lei'

    @pytest.mark.parametrize('suma, expected', [
        (800, 200),
        (1500, 1000),
        (0.99, 999.01),
        (0, 1000)
    ])
    def test_debitare_cont(self, suma, expected):
        self.titular.debitare_cont(suma)
        assert self.titular.sold == expected

    @pytest.mark.parametrize('suma, expected', [
        (350, 1350),
        (0, 1000),
        (0.99, 1000.99)
    ])
    def test_creditare_cont(self, suma, expected):
        self.titular.creditare_cont(suma)
        assert self.titular.sold == expected
