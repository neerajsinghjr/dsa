from goods_vehicle import GoodsVehicle
from offroad_vehicle import OffroadVehicle
from sports_vehicle import SportsVehicle
from normal_vehicle import NormalVehicle


def main():
    v1 = GoodsVehicle()
    v2 = OffroadVehicle()
    v3 = SportsVehicle()
    v4 = NormalVehicle()
    vehicles = [v1, v2, v3, v4]
    for vehicle in vehicles:
        print(f"Running: {vehicle.__class__.__name__} ...")
        vehicle.drive()


if __name__ == "__main__":
    main()