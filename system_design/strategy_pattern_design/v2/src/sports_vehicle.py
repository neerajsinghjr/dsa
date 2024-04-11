from vehicle import Vehicle
from drive_strategy.special_drive_strategy import SpecialDriveStrategy


class SportsVehicle(Vehicle):
    """
    Here SportsVehicle Class also used the same driving
    functionality used by the OffroadVehicle class.

    FIXED DUPLICACY ISSUE FROM V1 !!!
    """
    def __init__(self):
        super().__init__(SpecialDriveStrategy())
