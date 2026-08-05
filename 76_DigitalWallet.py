class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def add_money(self, amount):
        if(amount > 0):
            self.__balance = self.__balance + amount
        else:
            print("Invalid amount")

    def spend_money(self, amount):
        if(amount <= 0):
            print("Invalid amount")
        elif(amount > self.__balance):
            print("Insufficient balance")
        else:
            self.__balance = self.__balance - amount

    def display(self):
        print("Owner =", self.owner)
        print("Balance =", self.__balance)

w1 = Wallet("Tannu", 1000)

w1.display()

w1.add_money(500)
w1.display()

w1.spend_money(300)
w1.display()

w1.spend_money(2000)

w1.add_money(-50)

print(w1._Wallet__balance) # the mangled name is one underscore + class name + two underscores + variable name.


        