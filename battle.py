class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = []

    def attack(self, enemy):
        enemy.hp -= self.damage
        print(f"{self.name} атакує {enemy.name} на {self.damage} урону!")

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("Інвентар:")
        for item in self.inventory:
            print(f"- {item.name} ({item.value})")

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, player):
        player.hp -= self.damage
        print(f"{self.name} атакує {player.name} на {self.damage} урону!")

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

player = Player("Hero", 100, 20)
enemy = Enemy("Goblin", 50, 10)

sword = Item("Sword", 100)
potion = Item("Potion", 50)

player.add_item(sword)
player.add_item(potion)

player.show_inventory()

print("\nБій починається!\n")

while player.hp > 0 and enemy.hp > 0:
    player.attack(enemy)
    print(f"{enemy.name} HP: {enemy.hp}")

    if enemy.hp <= 0:
        print(f"{enemy.name} переможений!")
        break

    enemy.attack(player)
    print(f"{player.name} HP: {player.hp}")

    if player.hp <= 0:
        print(f"{player.name} програв!")