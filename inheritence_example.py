class Pets():
    animals = []
    def __init__(self,animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self,sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self,sounds):
        return f'{sounds}'

class Tommy(Cat):
    def sing(self,sounds):
        return f'{sounds}'

my_cats = [Simon('simon',3),Sally('sally',2),Tommy('tommy',1)]

my_pets = Pets(my_cats)

print(my_pets.walk())

