from .drive_strategy import DriveStrategy


class HeavyDriveStrategy(DriveStrategy):
    """
    HeavyDriveStrategy is used by Goods Vehicle.
    """
    def drive(self):
        print("Heavy lifting algorithm is working ...")
