import pytest
from sesiunea8.app.tema8_2 import Employee, BankAccount


class TestEmployee:
    def setup_method(self):
        self.employee = Employee('Popovici', 'Dumitru', 3000)

    def test_describe(self):
        assert self.employee.describe() == 'Emplyee`s first name: Popovici, last name: Dumitru, salary: 3000'

    def test_full_name(self):
        assert self.employee.full_name() == 'Popovici Dumitru'

    def test_monthly_salary(self):
        assert self.employee.monthly_salary() == 3000

    def test_annual_salary(self):
        assert self.employee.annual_salary() == 36000

    @pytest.mark.parametrize('percentage, expected', [
        (100, 6000),
        (0, 3000),
        (-50, 1500)
    ])
    def test_salary_review(self, percentage, expected):
        self.employee.salary_review(percentage)
        assert self.employee.salary == expected


class TestBankAccount:
    def setup_method(self):
        self.account_holder = BankAccount('RO1854241300011RON', 'Popescu Florin', 1000.00)

    def test_show_balance(self):
        assert self.account_holder.show_balance() == 'Account holder Popescu Florin with IBAN account RO1854241300011RON, has the current balance of 1000.00 RON'

    @pytest.mark.parametrize('amount, expected', [
        (800, 200),
        (1500, 1000),
        (0.99, 999.01),
        (0, 1000)
    ])
    def test_debit(self, amount, expected):
        self.account_holder.debit(amount)
        assert self.account_holder.balance == expected

    @pytest.mark.parametrize('amount, expected', [
        (350, 1350),
        (0, 1000),
        (0.99, 1000.99)
    ])
    def test_credit(self, amount, expected):
        self.account_holder.credit(amount)
        assert self.account_holder.balance == expected
