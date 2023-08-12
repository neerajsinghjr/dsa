class Vehicle:
    """
    Vehicle class is the base class which will be
    inherited by the further vehicle types.
    """
    def __init__(self, drive_strategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()
