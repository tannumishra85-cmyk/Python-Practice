class TV:
    def __init__(self, brand ,volume):
        self.brand = brand 
        self.volume = volume

    def volumeUp(self):
        if(self.volume >= 100):
            self.volume = 100
        else:
            self.volume += 1


    def volumeDown(self):
        if(self.volume <=0):
            self.volume = 0
        else:
            self.volume -= 1

    def display(self):
        print("Brand =", self.brand)
        print("Current Volume =", self.volume)

t1 = TV("LG" , 47)
t1.volumeUp()
t1.display()
t1.volumeDown()
t1.display()

    

    