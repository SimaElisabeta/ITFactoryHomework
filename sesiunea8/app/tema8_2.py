from dataclasses import dataclass


@dataclass
class Employee:
    first_name: str
    last_name: str
    salary: float

    def describe(self):
        return f'Emplyee`s first name: {self.first_name}, last name: {self.last_name}, salary: {self.salary}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def monthly_salary(self):
        return self.salary

    def annual_salary(self):
        return self.salary * 12

    def salary_review(self, percentage):
        calc_percentage = self.salary * (percentage * 0.01)
        self.salary = self.salary + int(calc_percentage)


@dataclass
class BankAccount:
    iban: str
    account_holder: str
    balance: float

    def show_balance(self):
        return f'Account holder {self.account_holder} with IBAN account {self.iban}, has the current balance of {self.balance:.2f} RON'

    def debit(self, amount):
        if amount > self.balance:
            print('Insufficient funds!')
        else:
            self.balance -= amount
            print(f"The amount of: {amount:.2f} RON, was debited from the account")

    def credit(self, amount):
        self.balance = self.balance + amount
