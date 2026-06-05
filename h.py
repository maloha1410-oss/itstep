class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
        self.inventory = []

    def info(self):
        print(f"\n{self.name} Level: {self.level} Health: {self.health}")

    def rest(self):
        self.health += 10
        print(f"{self.name} відпочиває.")

    def attack(self):
        print(f"{self.name} атакує.")

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("Inventory:", self.inventory)


class Warrior(Character):
    def __init__(self, name, level, health, energy):
        super().__init__(name, level, health)
        self.energy = energy

    def attack(self):
        print(f"{self.name} б'є мечем.")

    def strong_attack(self):
        if self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} використовує сильну атаку.")
        else:
            print("Недостатньо енергії.")


class Mage(Character):
    def __init__(self, name, level, health, mana):
        super().__init__(name, level, health)
        self.mana = mana

    def attack(self):
        print(f"{self.name} кидає заклинання.")

    def teleport(self):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} телепортується.")
        else:
            print("Недостатньо мани.")


class Archer(Character):
    def __init__(self, name, level, health, arrows):
        super().__init__(name, level, health)
        self.arrows = arrows

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            print(f"{self.name} стріляє з лука.")
        else:
            print("Немає стріл.")

    def dodge(self):
        print(f"{self.name} ухиляється.")


class BossMage(Mage):
    def attack(self):
        print(f"{self.name} викликає метеорит.")


warrior = Warrior("Arthur", 10, 100, 50)
mage = Mage("Merlin", 12, 80, 40)
archer = Archer("Robin", 8, 90, 5)
boss = BossMage("Dark Lord", 20, 200, 100)

warrior.add_item("Sword")
mage.add_item("Staff")
archer.add_item("Bow")

heroes = [warrior, mage, archer, boss]

for hero in heroes:
    hero.info()
    hero.attack()
    hero.show_inventory()

warrior.strong_attack()
mage.teleport()
archer.dodge()