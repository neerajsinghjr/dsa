from .enum import VehicleFees
from random import randint
from time import time

class Ticket:

    def __init__(self, vehicle, parking_slot):
        self.start_time = round(time())
        self.vehicle = vehicle
        self.parking_slot = parking_slot

    
    def create_ticket(self, vehicle):
        return f"{vehicle.id}-{round(time())}"
    

    def generate_bill(self, end_time=''):
        duration = round(time()) - self.start_time
        return VehicleFees.self.parking_lot()


    
               

