from .base_factory import BaseFactory
# from ..vehicle.maruti import Maruti
# from ..vehicle.hyundai import Hyundai
from vehicle.maruti import Maruti
from vehicle.hyundai import Hyundai


class StdFactory(BaseFactory):

    def get_type(type):
        try:
            vehicle = {
                'maruti': Maruti(),
                'hyundai': Hyundai()
            }

            return vehicle[type.lower()]

        except Exception as ex:
            print(f"Vehicle not found for type: {type}")
