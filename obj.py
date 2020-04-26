class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

harry = Employee("Harry", 34)
print(harry.salary)