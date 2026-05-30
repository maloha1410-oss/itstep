print("Коли над академією ШАГ повисла загроза повного знищення силами конкурентів, герої встали на її захист, вступаючи у двобої із суперниками")

import random

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def attack(self):
        return self.level * 5

    def defend(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def status(self):
        print(f"{self.name}: HP = {self.hp}, Level = {self.level}")

class Warrior(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
        self.armor = 5

    def attack(self):
        return self.level * 7 + random.randint(1, 5)

    def defend(self, damage):
        reduced_damage = max(0, damage - self.armor)
        self.hp -= reduced_damage
        if self.hp < 0:
            self.hp = 0

class Mage(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def attack(self):
        bonus = random.randint(5, 10)
        return self.level * 6 + bonus

    def defend(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

class Scout(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
        self.evasion = 0.3

    def attack(self):
        return self.level * 5 + random.randint(2, 8)

    def defend(self, damage):
        if random.random() < self.evasion:
            print(f"{self.name} ухилився від атаки!")
        else:
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_character(self, character):
        self.members.append(character)

    def total_power(self):
        return sum(member.level for member in self.members)

    def find_strongest(self):
        return max(self.members, key=lambda member: member.level)

class Arena:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.round_log = []

    def battle(self):
        round_number = 1

        print("\n ПОЧАТОК БОЮ")

        while self.fighter1.hp > 0 and self.fighter2.hp > 0:
            print(f"\nРаунд {round_number}")

            damage1 = self.fighter1.attack()
            self.fighter2.defend(damage1)

            print(f"{self.fighter1.name} атакує {self.fighter2.name} на {damage1} урону")

            if self.fighter2.hp <= 0:
                self.round_log.append(f"Раунд {round_number}: {self.fighter1.name} переміг")
                break

            damage2 = self.fighter2.attack()
            self.fighter1.defend(damage2)

            print(f"{self.fighter2.name} атакує {self.fighter1.name} на {damage2} урону")

            self.fighter1.status()
            self.fighter2.status()

            self.round_log.append(
                f"Раунд {round_number}: {self.fighter1.name} HP={self.fighter1.hp}, "
                f"{self.fighter2.name} HP={self.fighter2.hp}")

            round_number += 1

        winner = (
            self.fighter1
            if self.fighter1.hp > 0
            else self.fighter2
        )

        print(f"\nПереможець: {winner.name}")
        print(f"{winner.name} Захистив академію ШАГ!")

        print("\n ЛОГ БОЮ")
        for log in self.round_log:
            print(log)


def create_character(number):
    print(f"\nСтворення персонажа {number}")
    name = input("Ім'я: ")

    print("Оберіть клас:")
    print("1 - Warrior")
    print("2 - Mage")
    print("3 - Scout")

    choice = input("Ваш вибір: ")
    level = int(input("Рівень персонажа: "))

    if choice == "1":
        return Warrior(name, 120, level)
    elif choice == "2":
        return Mage(name, 90, level)
    else:
        return Scout(name, 100, level)

character1 = create_character(1)
character2 = create_character(2)

team = Team("Герої")
team.add_character(character1)
team.add_character(character2)

print("\n ІНФОРМАЦІЯ ПРО КОМАНДУ")
print("Загальна сила команди:", team.total_power())

strongest = team.find_strongest()
print(f"Найсильніший персонаж: {strongest.name} (Рівень {strongest.level})")

arena = Arena(character1, character2)
arena.battle()