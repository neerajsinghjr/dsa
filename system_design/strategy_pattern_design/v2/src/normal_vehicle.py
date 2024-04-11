from vehicle import Vehicle
from drive_strategy.general_drive_strategy import GeneralDriveStrategy


class NormalVehicle(Vehicle):
    """
    NormalVehicle Class is derived from vehicle base class
    which will use the heavy lifting driving algorithm.
    """
    def __init__(self):
        super().__init__(GeneralDriveStrategy())
