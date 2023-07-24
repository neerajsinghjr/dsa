from enum import Enum
from parking_slot import ParkingSlot


class VehicleType(Enum):

    SMALL = 'SMALL'
    LARGE = 'LARGE'
    COMPACT = 'COMPACT'
    BUSINESS = 'BUSINESS'
    HATCH_BACK = 'HATCH_BACK'
    TWO_WHEELER = 'TWO_WHEELER'


class VehicleFees(Enum):

    SMALL = lambda duration: duration * 100
    LARGE = lambda duration: duration * 300
    COMPACT = lambda duration: duration * 100
    BUSINESS = lambda duration: duration * 250
    HATCH_BACK = lambda duration: duration * 200
    TWO_WHEELER = lambda duration: duration * 50


class FloorMap:

    FLOOR = {
        
        VehicleType.LARGE.value : {
            'L1': ParkingSlot('L1', VehicleType.LARGE.value),
            'L2': ParkingSlot('L2', VehicleType.LARGE.value),
            'L3': ParkingSlot('L3', VehicleType.LARGE.value),
            'L4': ParkingSlot('L4', VehicleType.LARGE.value),
        },
        VehicleType.COMPACT.value : {
            'C1': ParkingSlot('C1', VehicleType.COMPACT.value),
            'C2': ParkingSlot('C2', VehicleType.COMPACT.value),
            'C3': ParkingSlot('C3', VehicleType.COMPACT.value),
            'C4': ParkingSlot('C4', VehicleType.COMPACT.value),
        },
        VehicleType.SMALL.value : {
            'S1': ParkingSlot('S1', VehicleType.SMALL.value),
            'S2': ParkingSlot('S2', VehicleType.SMALL.value),
            'S3': ParkingSlot('S3', VehicleType.SMALL.value),
            'S4': ParkingSlot('S4', VehicleType.SMALL.value),
        },
        VehicleType.BUSINESS.value : {
            'B1': ParkingSlot('B1', VehicleType.BUSINESS.value),
            'B2': ParkingSlot('B2', VehicleType.BUSINESS.value),
            'B3': ParkingSlot('B3', VehicleType.BUSINESS.value),
            'B4': ParkingSlot('B4', VehicleType.BUSINESS.value),
        }, 
        VehicleType.TWO_WHEELER.value : {
            'T1': ParkingSlot('T1', VehicleType.TWO_WHEELER.value),
            'T2': ParkingSlot('T2', VehicleType.TWO_WHEELER.value),
            'T3': ParkingSlot('T3', VehicleType.TWO_WHEELER.value),
            'T4': ParkingSlot('T4', VehicleType.TWO_WHEELER.value),
        },
        VehicleType.HATCH_BACK.value : {
            'H1': ParkingSlot('H1', VehicleType.HATCH_BACK.value),
            'H2': ParkingSlot('H2', VehicleType.HATCH_BACK.value),
            'H3': ParkingSlot('H3', VehicleType.HATCH_BACK.value),
            'H4': ParkingSlot('H4', VehicleType.HATCH_BACK.value),
        }
            
    }


