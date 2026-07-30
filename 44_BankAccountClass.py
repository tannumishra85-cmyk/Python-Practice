class BankAccount:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

    def deposit(self ,amount):
        self.balance = self.balance + amount
        print("Balance =", self.balance)

    def withdraw(self, amount):
        if(amount > self.balance):
            print("Insuffcient Balance")
        else:
            self.balance = self.balance - amount
            print("Balance =", self.balance)
        self.display()

    def display(self):
        print("Account Holder =",self.name)
        print("Current Balance =", self.balance)


acc = BankAccount("Tannu",1000)
acc.deposit(500)    
acc.withdraw(300)
        