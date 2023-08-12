from .drive_strategy import DriveStrategy


class GeneralDriveStrategy(DriveStrategy):
    """
    GeneralDriveStrategy is used by Normal Vehicle.
    """
    def drive(self):
        print("General driving algorithm is working ...")
