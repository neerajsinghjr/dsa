from abc import ABC, abstractmethod


class StockObservable(ABC):
    """
    StockObservable is a basic Observable Interface which
    includes the CRUD functionality of any observable
    - add() : Add observer to the observable list.
    - remove() : Remove observer from observable list.
    - notify() : Trigger notification to all observer, have a
    dependency injection for observable class.
    - set_date() : Update the core attribute of the observable
    date item.
    """
    @abstractmethod
    def add(self, oid, observer): ...

    @abstractmethod
    def remove(self, oid): ...

    @abstractmethod
    def notify(self): ...

    @abstractmethod
    def set_date(self, new_stock): ...
