
class SalaryCalculator:
    """
    SalaryCalculator : This interface will be used to calculate
    the actual salary of the employees of their respective
    department.
    """
    def generate_payroll(self, employees):
        print("Payroll System Started ...")
        print(f"Total Employees Found : {len(employees)}")
        for employee in employees:
            print("Employee: ",employee.name)
            print("- Salary Generated: ", employee.calculate_payroll())
