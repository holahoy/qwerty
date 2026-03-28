class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Player:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self, other):
        other.health -= self.weapon.damage
        print(f"{self.name} attacks {other.name} with {self.weapon.name} for {self.weapon.damage} damage.")

    def is_alive(self):
        return self.health > 0


sword = Weapon("Sword", 10)
axe = Weapon("Axe", 12)

player1 = Player("Hero", 30, sword)
player2 = Player("Enemy", 30, axe)

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    if player2.is_alive():
        player2.attack(player1)
    print(f"Health: {player1.name} = {player1.health}, {player2.name} = {player2.health}")

if player1.is_alive():
    print(f"{player1.name} wins!")
else:
    print(f"{player2.name} wins!")