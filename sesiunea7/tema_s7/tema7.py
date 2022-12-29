"""
a) ABSTRACTION
Clasa abstractă FormaGeometrica
* Conține un field PI=3.14
* Conține o metodă abstractă aria (opțional)
* Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’


b) INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
* Constructor pentru latură


c) ENCAPSULATION
Clasa Pătrat - latura este proprietate privată
* Implementează getter, setter, deleter pentru latură
* Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă: aria)

Clasa Cerc - moștenește FormaGeometrica
* Constructor pentru rază
Clasa Cerc - raza este proprietate privată
* Implementează getter, setter, deleter pentru rază
* Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte
(opțional, doar dacă ai ales să implementezi metoda abstractă aria)


d) POLYMORPHISM
* Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
* Creează un obiect de tip Pătrat și joacă-te cu metodele lui
* Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""

from abc import abstractmethod, ABC


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print("Cel mai probabil am colturi")


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, new_latura):
        self.__latura = new_latura

    @latura.deleter
    def latura(self):
        self.__latura = None

    def aria(self):
        return self.__latura ** 2


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, new_raza):
        self.__raza = new_raza

    @raza.deleter
    def raza(self):
        self.__raza = None

    def aria(self):
        return FormaGeometrica.PI * self.__raza ** 2

    def descriere(self):
        print('Eu nu am colturi')


patrat = Patrat(10)
patrat.descriere()
print(f'Latura initiala a patratului: {patrat.latura}')
print(f'Aria patratului: {patrat.aria()}')
patrat.latura = 4
print(f'Noua latura a patratului: {patrat.latura}')
print(f'Aria patratului: {patrat.aria()}')
del patrat.latura
print(f'Noua latura a patratului dupa DELETE: {patrat.latura} \n')

cerc = Cerc(5)
cerc.descriere()
print(f'Raza initiala a cercului: {cerc.raza}')
print(f'Aria cercului: {cerc.aria()}')
cerc.raza = 10
print(f'Raza noua a cercului: {cerc.raza}')
print(f'Aria cercului: {cerc.aria()}')
del cerc.raza
print(f'Noua raza a cercului dupa DELETE: {cerc.raza} \n')
