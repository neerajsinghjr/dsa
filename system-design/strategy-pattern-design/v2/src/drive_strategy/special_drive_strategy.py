from .drive_strategy import DriveStrategy


class SpecialDriveStrategy(DriveStrategy):
    """
    SpecialDrivingStrategy is used for SportsVehicle
    and OffroadVehicle etc.
    """
    def drive(self):
        print("Special driving algorithm is working ...")
