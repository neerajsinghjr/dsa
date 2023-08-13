from .base_factory import BaseFactory
# from ..vehicle.audi import Audi
# from ..vehicle.bmw import BMW
from vehicle.audi import Audi
from vehicle.bmw import BMW


class BizFactory(BaseFactory):

    def get_type(type):
        try:
            vehicle = {
                'audi': Audi(),
                'bmw': BMW()
            }

            return vehicle[type.lower()]

        except Exception as ex:
            print(f"Vehicle not found for type: {type}")
