
class SalaryCalculator:
    """
    SalaryCalculator : This interface will be used to calculate
    the actual salary of the employees of their respective
    department.
    """
    def generate_payroll(self, employees):
        print(f"Total Employees Found : {len(employees)}")
        for employee in employees:
            print("Employee: ", employee.name)
            print("- Salary Generated: ", employee.calculate_payroll())
            if employee.address:
                print("- Sent To: ", f"{employee.address.street}, "
                                     f"{employee.address.district}, "
                                     f"{employee.address.city}, "
                                     f"{employee.address.pincode}")
