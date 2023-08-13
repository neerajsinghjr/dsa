from stock_observable import StockObservable


class ElectronicObservable(StockObservable):
    """
    ElectronicObservable is an observable which handle
    observers related Phones.
    """
    def __init__(self, stock):
        # hold observer list;
        self.observers = {}
        self.stock = stock

    def add(self, oid, observer):
        if oid in self.observers:
            return
        self.observers[id] = observer

    def remove(self, oid):
        if oid in self.observers:
            del self.observers[oid]

    def notify(self):
        if not self.observers:
            return
        for observer in self.observers:
            observer.update()

    def set_date(self, new_stock):
        if self.stock == 0 and new_stock > 0:
            self.notify()
        self.stock += new_stock
