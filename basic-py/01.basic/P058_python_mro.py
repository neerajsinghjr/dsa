class Employee:
    def __init__(self, eid, name):
        self.id = eid
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self,  eid, name, salary):
        super().__init__(eid, name)
        self.salary = salary

    def calculate_payroll(self):
        return self.salary


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"Secretary: {self.name}, handled billing for {hours} hours")



class TemporarySecretary(Secretary):
    """
    final resolution:- MRO Method Resolution Order
    MRO for class TemporarySecretary(Secretary):
        <class 'TemporarySecretary'>,
        <class 'Secretary'>,
        <class 'SalaryEmployee'>,
        <class 'Employee'>,
        <class 'object'>
    )
    """
    def __init__(self, eid, name, hour, rate):
        # Need to control the constructor calling as well;;
        HourlyEmployee.__init__(self, eid, name, hour, rate)

    def calculate_payroll(self):
        # Needs to override this function as well;;
        return HourlyEmployee.calculate_payroll(self)


if __name__ == "__main__":
    shreya = TemporarySecretary(1005, "Janvi", 100, 70)