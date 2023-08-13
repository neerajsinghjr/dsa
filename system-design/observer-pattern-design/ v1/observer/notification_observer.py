from abc import ABC, abstractmethod


class NotificationObserver(ABC):
    """
    NotificationObserver is an observer interface which
    is used to implement Observer Class.
    - update()
    """
    def __init__(self, observable):
        self.observable = observable