from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def textile_amount(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def textile_amount(self):
        return self.v/6.5 + 0.5


coat = Coat(50)
print(coat.textile_amount)


class Suit(Clothes):

    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def textile_amount(self):
        return 2 * self.h + 0.5


suit = Suit(181)
print(suit.textile_amount)
