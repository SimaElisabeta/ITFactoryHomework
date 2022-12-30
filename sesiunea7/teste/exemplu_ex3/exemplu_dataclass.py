# varianta 1 (varianta obisnuita mai lunga, pentru care trebuie implementate separat
# metodele: __str__ , __repr__ sau __eq__)
print('***** Varianta 1 *****')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name: {self.name}, age: {self.age}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age


pA = Person('John', 25)
pB = Person('John', 25)
print(pA)
print(pA == pB)
print()

print('***** Varianta 2 *****')
# varianta 2 (varianta mai scurta, care are deja implementate mai multe metode)
from dataclasses import dataclass


@dataclass
class PersonAsDataclass:
    name: str
    age: int


p1 = PersonAsDataclass('John', 25)
p2 = PersonAsDataclass('John', 25)
print(p1)
print(p1 == p2)
