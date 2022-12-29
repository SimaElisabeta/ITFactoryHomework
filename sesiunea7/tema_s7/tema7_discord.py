"""
De raspuns la intrebarile:

1. Ce inseamna if __name__=="__main__" scris intr-un fisier python?
    * if __name__=="__main__" scris intr-un fisier python, este folosit pentru a permite sau pentru a preveni
    rularea unor parti de cod (irelevante sau relevante) atunci cand modulele sunt importate.
    * Astfel daca folosim if __name__=="__main__" in scriptul nostru, tot ce se afla in interiorului if-ului
    se va rula doar in fisierul main si nu va fi rulat in alte fisiere daca este importat

    (Referinte:
    https://www.youtube.com/watch?v=l3aRTwWanOE,
    https://www.youtube.com/watch?v=OBabwRH0XUo,
    https://www.freecodecamp.org/news/if-name-main-python-example/)

2. Cum instalam un pachet extern python?
    * Pachetele sunt o colectie de scrips care vor creste exponential capabilitatea de functionare a unui limbaj de programare
    * Pachetele python se pot accesa online la link-ul urmator (si nu numai): https://pypi.org/search/
    * Aceste pachete se pot instala folosind ?functia? package manager denumita pip
    (pip este un standard package management system, folosit pentru a instala pachete scrise in python)
    * Command prompt este una din interfatele de comanda (command line interface program) folosite pentru a executa
    comenzi in sistemele de operare windows

    (Referinte:
    https://www.youtube.com/watch?v=SrX5yo4KKGM
    https://pypi.org/search/)

3. Ce este dataclass in python?
4. Ce este functia hash?
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

