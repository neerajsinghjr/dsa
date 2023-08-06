import employees as e
from productivity_system import ProductivitySystem
from salary_calculator import SalaryCalculator


if __name__ == "__main__":
    e1 = e.Manager(1001, "Abhishek", 100000)
    e2 = e.SalesEmployee(1002, "Manoj", 40000, 4000)
    e3 = e.Secretary(1003, "Shreya", 50000)
    e4 = e.FactoryWorker(1004, "Ramesh", 234, 100)
    employees = [e1, e2, e3, e4]
    print("===============================")
    print("Productivity System Starting...")
    print("===============================")
    productivity_system = ProductivitySystem()
    productivity_system.trace_productivity(employees)

    print("==========================")
    print("Payroll System Starting...")
    print("==========================")
    payrolls = SalaryCalculator()
    payrolls.generate_payroll(employees)
