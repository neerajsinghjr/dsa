from main import ToppingMain


class VeggiesTopping(ToppingMain):
    """
    CheeseVeggies Topping is primary adds on the base 
    pizza price.
    CheeseVeggies Price is 20rs
    """
    def __init__(self, pizza):
        self.pizza = pizza
    
    def unit_price(self):
        return 20
    
    def cost(self):
        return f"{self.pizza.cost() + self.unit_price()}rs"
    