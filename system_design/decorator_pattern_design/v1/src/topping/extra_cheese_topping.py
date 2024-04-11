from main import ToppingMain


class ExtraCheeseTopping(ToppingMain):
    """
    ExtraCheeseTopping is primary adds on the base 
    pizza price.
    CheeseVeggies Price is 30rs
    """
    def __init__(self, pizza):
        self.pizza = pizza

    def unit_price(self):
        return 30
    
    def cost(self):
        return f"{self.pizza.cost() + self.unit_price()}rs"
    