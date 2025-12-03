class Employee:
    def __init__(self, emp_id, name, department):
        self.__emp_id = emp_id      
        self.name = name
        self.department = department
        self.company = "TechCorp"    

    def show_details(self):
        print(f"Employee ID: {self.__emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Company: {self.company}")

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, department, salary):
        super().__init__(emp_id, name, department)
        self.salary = salary

    def display(self):
        print(f"Monthly Salary: {self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, department, hourly_rate):
        super().__init__(emp_id, name, department)
        self.hourly_rate = hourly_rate

    def display(self):
        print(f"Hourly Rate: {self.hourly_rate}")

fte = FullTimeEmployee(101, "Harmeet", "IT", 45000)
pte = PartTimeEmployee(205, "Reema", "HR", 300)

fte.display()
fte.show_details()
print()
pte.display()
pte.show_details()
