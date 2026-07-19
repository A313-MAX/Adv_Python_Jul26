class Employee:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(self, employee_id, name, hours_worked, hourly_rate):
        super().__init__(employee_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class ContractEmployee(Employee):

    def __init__(self, employee_id, name, project_amount, bonus):
        super().__init__(employee_id, name)
        self.project_amount = project_amount
        self.bonus = bonus

    def calculate_salary(self):
        return self.project_amount + self.bonus


class Payroll:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def generate_payroll(self):
        total = 0

        for employee in self.employees:
            salary = employee.calculate_salary()

            print("\nEmployee ID :", employee.employee_id)
            print("Name :", employee.name)
            print("Salary : ₹", salary)

            total = total + salary

        print("\nTotal Payroll = ₹", total)


payroll = Payroll()

# Full Time Employee
print("Enter Full Time Employee Details")
eid = input("Employee ID: ")
name = input("Name: ")
salary = int(input("Monthly Salary: "))
emp1 = FullTimeEmployee(eid, name, salary)
payroll.add_employee(emp1)

# Part Time Employee
print("\nEnter Part Time Employee Details")
eid = input("Employee ID: ")
name = input("Name: ")
hours = int(input("Hours Worked: "))
rate = int(input("Hourly Rate: "))
emp2 = PartTimeEmployee(eid, name, hours, rate)
payroll.add_employee(emp2)

# Contract Employee
print("\nEnter Contract Employee Details")
eid = input("Employee ID: ")
name = input("Name: ")
project = int(input("Project Amount: "))
bonus = int(input("Bonus: "))
emp3 = ContractEmployee(eid, name, project, bonus)
payroll.add_employee(emp3)

print("\n------ Payroll Details ------")
payroll.generate_payroll()