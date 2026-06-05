class Animal:
    def __init__(self, name):
        self.name = name

class WildAnimal(Animal):
    def __init__(self, name, danger=True):
        super().__init__(name)
        self.danger = danger

class Predator(WildAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.food = [] 

    def add_food(self, animal):
        self.food.append(animal)

    def show_food(self):
        print(f"{self.name} eats:")
        for animal in self.food:
            print("-", animal)

class Lion(Predator):
    pass


class Tiger(Predator):
    pass


class Wolf(Predator):
    pass

class Herbivorous(WildAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.food = "grass"

    def eat(self):
        print(f"{self.name} eats {self.food}")

class Wildebeest(Herbivorous):
    pass


class Hare(Herbivorous):
    pass


class Deer(Herbivorous):
    pass

lion = Lion("Lion")
lion.add_food("Deer")
lion.add_food("Hare")

deer = Deer("Deer")

print("Dangerous:", lion.danger)
lion.show_food()

deer.eat()