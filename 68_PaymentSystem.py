class UPI():
    def pay(self):
        print("Payment through UPI")

class Card():
    def pay(self):
        print("Payemnt through Card")

class Cash():
    def pay(self):
        print("Payment through Cash")


Pay_Method = [UPI(), Card(), Cash()]

for pays in Pay_Method:
    pays.pay()