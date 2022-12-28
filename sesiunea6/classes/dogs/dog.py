class Dog:
    species = 'mammal'

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return f'age:{self.age}, name:{self.name}'

    def __repr__(self): 
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return False
        return self.age == other.age and self.name == other.name
