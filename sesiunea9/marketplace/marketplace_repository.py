import csv
import json
from abc import ABC, abstractmethod


class EntityNotFoundException(Exception):
    pass


class AbstractMarketplaceRepository(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass


class CSVMarketplaceRepository(AbstractMarketplaceRepository):
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    def read(self):
        if self.data:
            return self.data
        with open(self.file_name, "r") as f:
            reader = csv.reader(f)
            self.data = list(reader)
            return self.data

    def add(self, product):
        with open(self.file_name, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(product)
            self.data = None

    def delete(self, product_id):
        self.data = self.read()
        changed = False
        for elem in self.data:
            if elem[0] == product_id:
                changed = True
                self.data.remove(elem)
        if not changed:
            raise EntityNotFoundException(f'Entity with ID: {product_id} not found!')
        with open(self.file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)


class JSONMarketplaceRepository(AbstractMarketplaceRepository):
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    def read(self):
        if self.data:
            return self.data
        with open(self.file_name, 'r') as f:
            try:
                self.data = json.load(f)
            except:
                self.data = []
            return self.data

    def add(self, product):
        with open(self.file_name, 'w') as f:
            self.data = self.read()
            self.data.append(product)
            json.dump(self.data, f, indent=4)

    def delete(self, product_id):
        self.data = self.read()
        changed = False
        for elem in self.data:
            if str(elem.get("ID")) == product_id:
                changed = True
                self.data.remove(elem)
        if not changed:
            raise EntityNotFoundException(f'Entity with ID: {product_id} not found!')
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f, indent=4)
