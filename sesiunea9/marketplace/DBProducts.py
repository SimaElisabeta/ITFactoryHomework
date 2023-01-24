from dataclasses import dataclass


@dataclass()
class Product:
    name: str
    price: float

    def get_id(self):
        return abs(hash(self.name))

    def convert_to_list(self):
        return [self.get_id(), self.name, self.price]

    def convert_to_dict(self):
        return {'ID': self.get_id(), 'name': self.name, 'price': self.price}
