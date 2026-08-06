from abc import ABC, abstractmethod

class Character(ABC): # Abstract class
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    @abstractmethod
    def attack(self): # Abstract Method
        pass


    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        if(0 <= new_health <= 100):
            self.__health = new_health
        else:
            print("Invalid health")

    def take_damage(self, damage): # Normal method
        if(damage <= 0):
            print("Invalid damage")
        else:
            self.__health = self.__health - damage
            if(self.__health < 0):
                self.__health = 0
            print(self.name , "takes", damage , "damage")

    @abstractmethod
    def attack_damage(self):
        pass


    def battle(self, opponent):
        self.attack()
        opponent.take_damage(self.attack_damage()) # This is polymorphism in action.
        opponent.display()

    def display(self):
        print("Name =", self.name)
        print("Health =", self.__health)

# Children implement attack() in their own version ->> Method Overriding      
class Warrior(Character):
    def attack(self):
        print("Warrior attacks with sword")

    def attack_damage(self):
        return 30

class Mage(Character):
    def attack(self):
        print("Mage attacks with magic")

    def attack_damage(self):
        return 25

class Archer(Character):
    def attack(self):
        print("Archer shoots an arrow")

    def attack_damage(self):
        return 20





Characters = [Warrior("Tannu", 89), Mage("Aditya" , 100), Archer("Lucky", 100)]

for character in Characters:
    character.attack() # Same call but different objects give different results ->> Polymorphism

Characters[0].set_health(70) # Getter & Setter
print(Characters[0].get_health())

Characters[0].display()
Characters[1].display()
Characters[2].display()

character.attack() # Notice : Here character is temporarrily referals.. 
# after loop finishes, character still refers to the last object.
character.take_damage(20)
character.display()


Characters[0].battle(Characters[1]) # Characters[0] vs Characters[1]
Characters[1].battle(Characters[2]) 
Characters[2].battle(Characters[0]) 
# An object can be passed as an argument to another object's method.

# Character       → class
# Characters      → list
# Characters[0]   → Warrior object
# Characters[1]   → Mage object
# Characters[2]   → Archer object
# character       → loop variable