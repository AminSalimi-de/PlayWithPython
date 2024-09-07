
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        
    def fullName(self):
        return f"{self.first} {self.last}"

emp1 = Employee("Amin", "Salimi")

print(emp1.fullName())
print(emp1.email)