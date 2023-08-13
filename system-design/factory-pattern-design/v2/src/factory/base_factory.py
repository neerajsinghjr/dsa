from abc import ABC, abstractmethod


class BaseFactory(ABC):

    @abstractmethod
    def get_type(type): ...
