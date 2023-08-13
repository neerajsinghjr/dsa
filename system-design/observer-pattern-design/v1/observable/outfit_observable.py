from .stock_observable import StockObservable


class OutfitObservable(StockObservable):
    """
    ElectronicObservable is an observable which handle
    observers related Phones.
    """
    def __init__(self, stock=0):
        self.stock = stock
        self.observers = []

    def add(self, observer):
        if observer in self.observers:
            return
        if isinstance(observer, list):
            self.observers.extend(observer)
        else:
            self.observers.append(observer)

    def remove(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        if not self.observers:
            return
        for observer in self.observers:
            observer.update()

    def set_data(self, new_stock):
        if self.stock == 0 and new_stock > 0:
            self.notify()
        self.stock += new_stock
