from shape.circle import Cirle
from shape.triangle import Triangle
from shape.rectangle import Rectangle


class ShapeFactory:

    @staticmethod
    def get_shape(type):
        try:
            shapes = {
                'circle': Cirle(),
                'triangle': Triangle(),
                'rectangle': Rectangle()
            }

            return shapes[type.lower()]

        except Exception as ex:
            print(f"Error: Shape of type: {type} not found")
