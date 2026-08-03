class Employee:
    def work(self):
        print("Employees are working..")

class Developer(Employee):
    def work(self):
        print("Developer writes code")
        

class Designer(Employee):
    def work(self):
        print("Designer creates designs")

employees = [Developer(), Designer()]

for employee in employees:
    employee.work()
