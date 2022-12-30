"""
De raspuns la intrebarile:

1. Ce inseamna if __name__=="__main__" scris intr-un fisier python?
    * if __name__=="__main__" scris intr-un fisier python, este folosit pentru a permite sau pentru a preveni
    rularea unor parti de cod atunci cand modulele sunt importate.
    * Astfel daca folosim if __name__=="__main__" in scriptul nostru, tot ce se afla in interiorului if-ului
    se va rula doar in fisierul main (la runtime) si nu va fi rulat in alte fisiere daca este importat

    (Referinte:
    https://www.youtube.com/watch?v=l3aRTwWanOE,
    https://www.youtube.com/watch?v=OBabwRH0XUo,
    https://www.freecodecamp.org/news/if-name-main-python-example/)


2. Cum instalam un pachet extern python?
    * Pachetele python se pot accesa online la link-ul urmator (si nu numai): https://pypi.org/search/
    * Command prompt este una din interfatele de linie de comanda folosite pentru a executa comenzi in sistemele
    de operare windows. Ne vom folosi de aceasta pagina de comanda pentru instalarea unor pachete in python
    * Astfel, vom deschide command prompt din windows. Inainte de a incepe instalarea trebuie urmati anumiti pasi
    pentru a ne asigura ca avem conditiile necesare de instalare:
        1. Trebuie sa ne asiguram ca avem python instalat pe computer tastand in command prompt
        urmatoarea comanda: python --version
            a) Daca avem python instalat, atunci la tastarea comenzii ar trebui sa primim un output cu versiunea
                de python instalata.
            b) Daca nu avem python instalat vom primi o eroare si va trebui sa instalam versiunea oficiala de python
                pe care o putem descarca gratuit de pe internet.
        2. Vom testa daca avem instalat tool-ul pip prin urmatoarea comanda: pip -- version
        (pip ar trebui sa fie deja instalat pe computer odata ce am instalat versiune oficiala de python,
        pip este un standard package management system, folosit pentru a instala pachete scrise in python)
            a) Daca avem pip instalat, atunci la tastarea comenzii ar trebui sa primim un output cu versiunea
                de pip curenta.
            b) Daca nu avem tool-ul pip instalat atunci vom primi o eroare. Pentru a instala pip vom folosi urmatoarea
                linie de comanda: python -m ensurepip --default -pip
        3. Ne vom asigura ca toate mecanismele de instalare sunt la ultima versiune, folosind comanda:
        python -m pip install --upgrade pip setuptools wheel
    * Dupa ce am urmarit toti pasii de mai sus, pentru a instala anumie pachete vom folosi linia de comanda:
    pip install +denumirea pachetului pe care dorim sa il instalam (ex: pip install numpy sau pip install pybrot)

    (Referinte:
    https://www.youtube.com/watch?v=SrX5yo4KKGM
    https://pypi.org/search/)


3. Ce este dataclass in python?
    * Dataclass in python sunt clase care permit definirea claselor intr-un mod mai simplu, folosind mai putine linii de cod
    * Clasele de tip dataclass au deja implementate o varietate de metode precum: __str__ , __repr__ sau __eq__,
    fata de clasele obisnuite la care trebuie implementata fiecare metoda manual
    * Pentru a crea o clasa de tip dataclass se va importa: from dataclasses import dataclass
    si se va folosi decoratorul @dataclass

    (Referinte:
    https://www.pythontutorial.net/python-oop/python-dataclass/
    https://www.pythoncheatsheet.org/cheatsheet/dataclasses)


4. Ce este functia hash?
    * Funcatia hash() primeste un obiect si genereaza un numar intreg. Pentru acelasi input tot timpul va
    returna aceeasi valoare
    * Atunci cand pasam un obiect functiei hash(), Python va executa metoda speciala __hash__ a obiectului

    exemplu:
    Syntax : hash(obj)
    Parameters :  obj : The object which we need to convert into hash.
    Python will call the __hash__ method of the p1 object: p1.__hash__()
    Returns : Returns the hashed value if possible.

    (Referinte:
    https://www.pythontutorial.net/python-oop/python-__hash__/
    https://www.geeksforgeeks.org/python-hash-method/)


5. Cum pot face codul de mai jos sa functioneze corect?

    class Person:
        def __init__(self, age, name):
            self.age = age
            self.name = name
    
        def __eq__(self, other):
            return isinstance(other, Person) and self.age == other.age and self.name == other.name

    s = set()
    p = Person(29, "Adrian")
    s.add(p)

De urmarit cursul [https://www.w3schools.com/html/default.asp]
De urmarit cursul [https://www.w3schools.com/css/default.asp]
"""

# Exercitiul 5
# Varianta 1
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age and self.name == other.name

    def __hash__(self):
        return hash(self.age) + hash(self.name)


s = set()
p = Person(29, "Adrian")
s.add(p)
print(s)

# Varianta 2
from dataclasses import dataclass, astuple


@dataclass
class PersonAsDataclass:
    age: int
    name: str


s2 = set()
p2 = PersonAsDataclass(29, "Adrian")
s2.add(astuple(p2))
print(s2)
