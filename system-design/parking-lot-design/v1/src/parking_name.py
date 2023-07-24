
class ParkingName:

    def __init__(self, name, address='') -> None:
        self.name = name
        self.address = address


    def __repr__(self) -> str:
        return f"Parking: {self.name}"