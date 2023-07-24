class ParkingAddress:

    def __init__(self, street, city, pincode):
        self.street = street
        self.city = city
        self.pincode = pincode


    def __repr__(self) -> str:
        return f"Goto: {self.street}, {self.city} {self.pincode}"