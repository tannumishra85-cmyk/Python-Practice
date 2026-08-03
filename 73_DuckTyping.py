class Printer:
    def work(self):
        print("Printing document")


class Scanner:
    def work(self):
        print("Scanning document")


class Camera:
    def click(self):
        print("Photo clicked")


def use_machine(machine):  # It'll give us error of AttributeError.
    machine.work() 


machines = [Printer(), Scanner(), Camera()]

for machine in machines:
    use_machine(machine)


