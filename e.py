import random

print("Коли над академією ШАГ повисла загроза повного знищення силами конкурентів, герої встали на її захист.")

class Character:
    def __init__(self, name, hp, level):
        self.name, self.hp, self.level = name, hp, level

    def attack(self):
        return self.level * 5

    def defend(self, damage):
        self.hp = max(0, self.hp - damage)

    def status(self):
        print(f"{self.name}: HP={self.hp}, Level={self.level}")


class Warrior(Character):
    armor = 5

    def attack(self):
        return self.level * 7 + random.randint(1, 5)

    def defend(self, damage):
        self.hp = max(0, self.hp - max(0, damage - self.armor))


class Mage(Character):
    def attack(self):
        return self.level * 6 + random.randint(5, 10)


class Scout(Character):
    evasion = 0.3

    def attack(self):
        return self.level * 5 + random.randint(2, 8)

    def defend(self, damage):
        if random.random() < self.evasion:
            print(f"{self.name} ухилився!")
        else:
            self.hp = max(0, self.hp - damage)


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_character(self, character):
        self.members.append(character)

    def total_power(self):
        return sum(c.level for c in self.members)

    def find_strongest(self):
        return max(self.members, key=lambda c: c.level)


class Arena:
    def __init__(self, f1, f2):
        self.f1, self.f2 = f1, f2

    def battle(self):
        round_num = 1

        while self.f1.hp > 0 and self.f2.hp > 0:
            print(f"\nРаунд {round_num}")

            dmg = self.f1.attack()
            self.f2.defend(dmg)
            print(f"{self.f1.name} атакує {self.f2.name} на {dmg}")

            if self.f2.hp <= 0:
                break

            dmg = self.f2.attack()
            self.f1.defend(dmg)
            print(f"{self.f2.name} атакує {self.f1.name} на {dmg}")

            self.f1.status()
            self.f2.status()
            round_num += 1

        winner = self.f1 if self.f1.hp > 0 else self.f2
        print(f"\nПереможець: {winner.name}")
        print(f"{winner.name} захистив академію ШАГ!")


def create_character(num):
    print(f"\nСтворення персонажа {num}")
    name = input("Ім'я: ")
    choice = input("Клас (1-Warrior, 2-Mage, 3-Scout): ")
    level = int(input("Рівень: "))

    if choice == "1":
        return Warrior(name, 120, level)
    if choice == "2":
        return Mage(name, 90, level)
    return Scout(name, 100, level)


c1 = create_character(1)
c2 = create_character(2)

team = Team("Герої")
team.add_character(c1)
team.add_character(c2)

print("\nЗагальна сила команди:", team.total_power())
print("Найсильніший:", team.find_strongest().name)

Arena(c1, c2).battle()