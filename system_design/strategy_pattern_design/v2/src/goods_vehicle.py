from vehicle import Vehicle
from drive_strategy.heavy_drive_strategy import HeavyDriveStrategy


class GoodsVehicle(Vehicle):
    """
    GoodsVehicle is driving from Vehicle class
    with general driving algorithm.
    """
    def __init__(self):
        super().__init__(HeavyDriveStrategy())
