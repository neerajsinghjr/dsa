import hr
from salary_calculator import SalaryCalculator


if __name__ == "__main__":
    e1 = hr.SalaryEmployee(1001, "Abhishek", 30000)
    e2 = hr.CommissionEmployee(1002, "Manoj", 30000, 2000)
    e3 = hr.HourlyEmployee(1003, "Shreya", 234, 100)
    payrolls = SalaryCalculator()
    payrolls.generate_payroll([e1, e2, e3])
