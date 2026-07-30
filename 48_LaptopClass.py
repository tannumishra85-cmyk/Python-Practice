class Laptop:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def use(self, hours):
        self.battery = self.battery - (hours * 10)

    def charge(self):
        self.battery = 100

    def display(self):
        print("Brand =", self.brand)
        print("Current battery percentage =", self.battery)


l1 = Laptop("Dell", 100)
l1.use(3)
l1.display()
l1.charge()
l1.display()  
        