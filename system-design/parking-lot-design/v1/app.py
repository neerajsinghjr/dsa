from src.ticket import Ticket
from src.vehicle import Vehicle
from time import time, sleep
from src.parking_name import ParkingName
from src.parking_floor import ParkingFloor
from src.parking_address import ParkingAddress
from src.enum import (VehicleFees, VehicleType, FloorMap)


if __name__ == "__main__":
    # floor count;;
    count = 10

    # create vehicle;;
    parking_addr = ParkingAddress("Main Street", "Downtown", 2001010)
    parking_name = ParkingName(
        name = "Devilish Parking Zone", 
        address= parking_addr
    )
    
    # parking floors;;
    total_floors = {f"{1}f" : FloorMap.value for i in range(1, count+1)}
    print("all_floor :", total_floors)
    parking_floors = ParkingFloor(total_floors)

    # assign vehicle type;;
    bike = Vehicle(
        id="DL-10-SU0726",
        name="Ntorq Scooty", 
        type=VehicleType.TWO_WHEELER.value
    )

    # check if parking_slot is available for particular type;
    parking_slot = parking_floors.get_relevant_parking_and_park(Vehicle=bike)

    # if available then assign and make payment;;
    if parking_floors:
        # else, notify ticket counter;;
        ticket = Ticket(
            vehicle=bike,
            parking_slot=parking_slot
        )
        ticket_no = ticket.create_ticket
        print(f"Ticket Generated For Vehicle {bike.id} : {ticket_no}")
        sleep(1000)
        bill = ticket.generate_bill()
        print(f"Amount to be paid in {bill}rs")
                
    else:
        # TODO: Re-assign with some allocated space;;
        print(f"Parking Slot for Vehicle Type: {bike.type} not available !")
