class Character:   # Basic game character
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display(self):
        print("Name =", self.name)
        print("Health =", self.health)

    def attack(self):
        print("Character attacks")

    def take_damage(self, damage):
        self.health = self.health - damage
        if(self.health < 0):
            self.health = 0
        print(self.name , "takes", damage , "damage")

class Warrior(Character):  # Special type of character
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        print("Warrior attacks with", self.weapon)

class EliteWarrior(Warrior): # Advanced warrior
    def __init__(self, name, health, weapon, level):
        super().__init__(name, health, weapon)
        self.level = level

    def display(self):
        print("Name =", self.name)
        print("Health =", self.health)
        print("weapon =", self.weapon)
        print("Level =", self.level)

    def attack(self):
        print("Elite Warrior attacks with", self.weapon , "at level", self.level)

    
e1 = EliteWarrior("Tannu", 100 , "Sword", 5)
e1.display()
e1.attack()
e1.take_damage(30)
