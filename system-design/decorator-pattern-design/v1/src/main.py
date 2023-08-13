from abc import ABC, abstractmethod


class PizzaMain(ABC):
    """
    PizzaMain is the base class of the pizza.
    Every Pizza Class will directly inherit it
    and will implement its respective functions.
    """
    @abstractmethod
    def cost(self): ...


class ToppingMain(PizzaMain):
    """
    PizzaMain <- ToppingMain

    ToppingMain is the main class for topping.
    Every topping child class will derive from
    it for further extra addition of cost.
    """
    @abstractmethod
    def cost(self): ...
