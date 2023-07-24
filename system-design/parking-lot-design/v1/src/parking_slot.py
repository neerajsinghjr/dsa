
class ParkingSlot:
    
    def __init__(self, name, slot_type):
        self.name = name
        self.type = slot_type
        self.is_free = True
        self.vehicle = None

    
    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.is_free = False

    
    def remove_vehicle(self):
        self.vehicle = None
        self.is_free = True