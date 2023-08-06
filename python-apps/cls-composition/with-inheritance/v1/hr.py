from abc import ABC, abstractmethod


class Employee:
    """
    Employee: Base class contains the basic details of employee
    eid represent employee_id
    name represent employee_name
    """
    def __init__(self, eid, name):
        self.id = eid
        self.name = name

    @abstractmethod
    def calculate_payroll(self): ...


class SalaryEmployee(Employee):
    """
    SalaryEmployee: SalaryEmployee derives from the employee class
    and payroll calculated on the basis of

    """
    def __init__(self,  eid, name, salary):
        super().__init__(eid, name)
        self.salary = salary

    def calculate_payroll(self):
        return self.salary


class HourlyEmployee(Employee):

    def __init__(self, eid, name, hour, rate):
        super().__init__(eid, name)
        self.hour = hour
        self.rate = rate

    def calculate_payroll(self):
        return self.hour * self.rate


class CommissionEmployee(SalaryEmployee):
    """
    CommissionEmployee: These are those employee which gets extra
    perks on the fixed employee salary
    """
    def __init__(self, eid, name, salary, perks):
        super().__init__(eid, name, salary)
        self.perks = perks

    def calculate_payroll(self):
        return super().calculate_payroll() + self.perks
