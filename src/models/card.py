"""
    A class to describe card.
"""

from enum import Enum, unique


@unique
class Type(Enum):
    """The type of cards which will be a enum type"""
    slash = 0
    dodge = 1
    peach = 2


class Cards(object):
    """Represent the cards"""

    def __init__(self, title, typeOfCard, point):
        self._title = title
        self._type = typeOfCard
        self._point = point

    @property
    def title(self):
        return self._title

    @property
    def type(self):
        return self._type

    @property
    def point(self):
        return self._point
