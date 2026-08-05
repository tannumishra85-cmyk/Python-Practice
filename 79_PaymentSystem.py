from abc import ABC, abstractmethod

class Payment(ABC):
    # The program also will work without inherit ABC but,
    # with ABC python enforce the abstract class rule

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Payment through UPI")

class Card(Payment):
    def pay(self):
        print("Payment through Card")

u1 = UPI()
u1.pay()

c1 = Card()
c1.pay()

