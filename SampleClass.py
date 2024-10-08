import datetime

class Employee:
    num_of_employees = 0
    raise_coeff = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleting fullname!")
        self.first = None
        self.last = None

    def appply_raise(self):
        self.pay *= self.raise_coeff
        
    def print(self):
        print(f"Name={self.fullname}")
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

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self) -> str:
        return f"Name={self.fullname} - email={self.email}" 

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)
    
class Developer(Employee):
    raise_coeff = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees==None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_employee(self, emp)    :
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname)


emp1 = Employee("Amin", "Salimi", 50000)
emp2 = Employee("Taghi", "Tsghizadeh", 60000)
emp3_str = "Naghi-Naghizadeh-70000"
emp3 = Employee.from_string(emp3_str)

emp1.raise_coeff = 1.05
emp1.appply_raise()

emp1.print()
emp2.print()
emp3.print()

dev1 = Developer("Ozra", "Fahimi", 40000, "Python")

mngr1 = Manager("Omid", "Razegi", 100000, [dev1])
mngr1.add_employee(emp1)
mngr1.add_employee(emp2)
mngr1.remove_employee(dev1)

print()
print(Employee.is_work_day(datetime.date(2024, 9, 7)))
print(Employee.raise_coeff)
print(Employee.num_of_employees)
print(dev1.email)
print(mngr1.fullname)
mngr1.print_employees()
#print(help(Manager))
print(isinstance(mngr1, Manager))
print(issubclass(Manager, Employee))

print(emp1)
print(emp1+emp2)
print(len(emp1))

emp1.first = "Amir"
print(emp1)

emp1.fullname = "Jaber Hayyan"
print(emp1)

del emp1.fullname
print(emp1)