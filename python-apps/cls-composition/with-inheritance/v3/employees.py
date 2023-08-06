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


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"Manager: {self.name}, yells for {hours} hours")


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"Secretary: {self.name}, handled billing for {hours} hours")


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f"Factory Worker: {self.name}, manufactured for {hours} hours")


class SalesEmployee(CommissionEmployee):
    def work(self, hours):
        print(f"Sales Employees: {self.name}, increase sales by {hours} hours")


class TemporarySecretary(Secretary, HourlyEmployee):
    """
    Constraints 3
    We add new TemporarySecretary who works as Secretary
    but wages calculated on hourly basis.

    Countermeasure for Multiple Inheritance
    case 1:
    class TemporarySecretary(HourlyEmployee, Secretary):
    Doesn't work thrown error;;

    case 1.1:
    class TemporarySecretary(Secretary, HourlyEmployee):
    Doesn't work, thrown error;;

    case 2:
    Tried, Creating __init__() and then calling super()

    final resolution:- MRO Method Resolution Order
    MRO for class TemporarySecretary(HourlyEmployee, Secretary):
    Order 1 : (
        <class 'TemporarySecretary'>,
        <class 'HourlyEmployee'>,
        <class 'Secretary'>,
        <class 'SalaryEmployee'>,
        <class 'Employee'>,
        <class 'object'>
    )

    MRO for class TemporarySecretary(Secretary, HourlyEmployee):
    Order 2 : (
        <class 'TemporarySecretary'>,
        <class 'Secretary'>,
        <class 'SalaryEmployee'>,
        <class 'HourlyEmployee'>,
        <class 'Employee'>,
        <class 'object'>
    )

    So we prefer MRO Order 2 because in MRO order 1,
    TemporarySecretary -> HourlyEmployee -> Secretary
    In this case, even if you override the HourlyEmployee
    then, next lineup will be called and the Secretary class
    will throw error of missing argument named 'salary'

    that's why we reverse the order,
    class TemporarySecretary(HourlyEmployee, Secretary):
    class TemporarySecretary(Secretary, HourlyEmployee):

    Now HourlyEmployee -> Employee will work successfully.
    """
    def __init__(self, eid, name, hour, rate):
        # Need to control the constructor calling as well;;
        HourlyEmployee.__init__(self, eid, name, hour, rate)

    def calculate_payroll(self):
        # Needs to override this function as well;;
        return HourlyEmployee.calculate_payroll(self)
