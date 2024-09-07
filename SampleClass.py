import datetime

class Employee:
    num_of_employees = 0
    raise_coeff = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay
        Employee.num_of_employees += 1
           
    def fullName(self):
        return f"{self.first} {self.last}"

    def appply_raise(self):
        self.pay *= self.raise_coeff
        
    def print(self):
        print(f"Name={self.fullName()}")
        print(f"email={self.email}")
        print(f"raise_coeff={self.raise_coeff}")
        print(f"pay={self.pay}")
        print()
        
    @classmethod
    def from_string(cls, empl_str):
        first, last, pay = empl_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_work_day(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True        
    
emp1 = Employee("Amin", "Salimi", 50000)
emp2 = Employee("Taghi", "Tsghizadeh", 60000)
emp3_str = "Naghi-Naghizadeh-70000"
emp3 = Employee.from_string(emp3_str)

emp1.raise_coeff = 1.05

emp1.appply_raise()

emp1.print()
emp2.print()
emp3.print()

print()
print(Employee.is_work_day(datetime.date(2024, 9, 7)))
print(Employee.raise_coeff)
print(Employee.num_of_employees)

