from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


# REAL LIFE example - exercise 1
class HouseBuilder(ABC):
    @property
    @abstractmethod
    def house(self) -> None:
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_garage(self):
        pass

    @abstractmethod
    def build_pool(self):
        pass

    @abstractmethod
    def build_garden(self):
        pass


class ConcreteHouseBuilder1(HouseBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._house = House1()

    @property
    def house(self) -> House1:
        house = self._house
        self.reset()
        return house

    def build_walls(self):
        self._house.add("Walls")

    def build_doors(self):
        self._house.add("Doors")

    def build_windows(self):
        self._house.add("Windows")

    def build_roof(self):
        self._house.add("Roof")

    def build_garage(self):
        self._house.add("Garage")

    def build_pool(self):
        self._house.add("Pool")

    def build_garden(self):
        self._house.add("Garden")


class House1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"House contains: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._house_builder = None

    @property
    def house_builder(self) -> HouseBuilder:
        return self._house_builder

    @house_builder.setter
    def house_builder(self, house_builder: HouseBuilder) -> None:
        self._house_builder = house_builder

    def build_minimal_viable_product(self) -> None:
        self.house_builder.build_walls()
        self.house_builder.build_roof()
        self.house_builder.build_doors()
        self.house_builder.build_windows()

    def build_full_featured_product(self) -> None:
        self.house_builder.build_walls()
        self.house_builder.build_roof()
        self.house_builder.build_doors()
        self.house_builder.build_windows()
        self.house_builder.build_garage()
        self.house_builder.build_pool()


director = Director()
house_builder = ConcreteHouseBuilder1()
director.house_builder = house_builder

print("Standard basic product: ")
director.build_minimal_viable_product()
house_builder.house.list_parts()

print("\n")

print("Standard full featured product: ")
director.build_full_featured_product()
house_builder.house.list_parts()

print("\n")

print("Custom product: ")
house_builder.build_walls()
house_builder.build_roof()
house_builder.build_doors()
house_builder.build_windows()
house_builder.build_garage()
house_builder.build_garden()
house_builder.build_pool()
house_builder.house.list_parts()
