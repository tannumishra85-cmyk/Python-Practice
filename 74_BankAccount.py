class BankAccount:
    def __init__(self,owner, _balance):
        self.owner = owner
        self._balance = _balance

    def deposit(self,amount):
        self._balance = self._balance + amount

    def withdraw(self, amount):
        if(self._balance < amount):
            print("Insufficient balance")
        else:
            self._balance = self._balance - amount

    def display_balance(self):
        print("Current balance =", self._balance)

a1 = BankAccount("Tannu", 5000)

a1.display_balance()
a1.deposit(1000)
a1.display_balance()
a1.withdraw(2000)
a1.display_balance()
a1.withdraw(10000)