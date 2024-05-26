from abc import ABC, abstractmethod

class Scene(ABC) :
    @abstractmethod
    def Setup(self): pass

    @abstractmethod
    def Update(self): pass

    @abstractmethod
    def Exit(self): pass