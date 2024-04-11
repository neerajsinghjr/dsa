from pizza import (
    Margherita, 
    VegDelight, 
    SpicyCheese, 
    CheeseMountain
)
from topping import (
    VeggiesTopping,
    ExtraCheeseTopping, 
    CheeseVeggiesTopping
)


def main():
    bp1 = VegDelight()
    bpt1 = ExtraCheeseTopping(pizza=bp1)
    bp2 = SpicyCheese()
    bpt2 = CheeseVeggiesTopping(pizza=bp2)
    bp3 = CheeseMountain()
    bpt3 = CheeseVeggiesTopping(pizza=bp3)
    bp4 = Margherita()
    bpt4 = VeggiesTopping(pizza=bp4)

    orders = [(bp1, bpt1), (bp2, bpt2), (bp3, bpt3), (bp4, bpt4)]

    for pizza, topping in orders:
        print("=========================================================")
        print("|------------------ ORDER DETAILS ----------------------|")
        print("=========================================================")
        print(f"Base Pizza ({pizza.__class__.__name__}) : {pizza.cost()}.00 rs")
        print(f"Base Topping ({topping.__class__.__name__}) : {topping.unit_price()}.00 rs")
        print(f"Total Order Summary  ({pizza.__class__.__name__}) : {topping.cost()}.00 rs")
        print("=========================================================")
        print("\n")
        

if __name__ == "__main__":
    main()