from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def info(self): ...
