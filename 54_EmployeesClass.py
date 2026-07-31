class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary


    def increase_salary(self,percent):
        self.salary = (self.salary*percent)/100 + self.salary

    def display(self):
        print("Name =", self.name)
        print("Salary =", self.salary)


    


e1 = Employee("Tannu" , 30000)
e1.display()
e1.increase_salary(10)
e1.display()
        