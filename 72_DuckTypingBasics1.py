class Car:
    def start(self):
        print("Car engine starts")

class Computer:
    def start(self):
        print("Computer starts")

class WashingMachine:
    def start(self):
        print("Washing Machine starts")

def start_device(device):
    device.start()

start_device(Car())
start_device(Computer())
start_device(WashingMachine())