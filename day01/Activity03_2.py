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

employees = []

for i in range(1, 201):
    print(f"\nEnter details for Employee {i}:")
    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    department = input("Department: ")
    emp_type = input("Type (F for Full-Time / P for Part-Time): ").upper()
    
    if emp_type == "F":
        salary = float(input("Monthly Salary: "))
        emp = FullTimeEmployee(emp_id, name, department, salary)
    else:
        hourly_rate = float(input("Hourly Rate: "))
        emp = PartTimeEmployee(emp_id, name, department, hourly_rate)
    
    employees.append(emp)

for emp in employees:
    emp.display()
    emp.show_details()
    print("-" * 40)
