import employees as e
from address import Address
from productivity_system import ProductivitySystem
from salary_calculator import SalaryCalculator


if __name__ == "__main__":
    e1 = e.Manager(1001, "Abhishek", 100000)
    e1.address = Address("12 Block", "North Delhi", "Delhi", "110099")
    e2 = e.SalesEmployee(1002, "Manoj", 40000, 4000)
    e2.address = Address("20 Block", "East Delhi", "Delhi", "110099")
    e3 = e.Secretary(1003, "Shreya", 50000)
    e3.address = Address("12 Block", "North East Delhi", "Delhi", "110099")
    e4 = e.FactoryWorker(1004, "Ramesh", 234, 100)
    e4.address = Address("12 Block", "West Delhi", "Delhi", "110099")
    # e5: Temporary Secretary with multiple inheritance constraints;;
    e5 = e.TemporarySecretary(1005, "Janvi", 100, 70)
    e5.address = Address("12 Block", "South Delhi", "Delhi", "110099")
    employees = [e1, e2, e3, e4, e5]
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
