class Mobile:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def use(self, hours):
        self.battery = self.battery - (hours * 10)
        if(self.battery <= 0):
            self.battery = 0
        

    def charge(self):
        self.battery = 100 

    def display(self):
        print("Brand =", self.brand)
        print("Battery =", self.battery)

m1 = Mobile("Samsung" , 89)
m1.display()
m1.use(2)
m1.display() 
m1.charge()
m1.display()      