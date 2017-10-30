"""
Model represent the stage of game.

There are only six kinds of stage for each game:
* starting
* judgment
* getCards
* useCards
* discard
* ending
"""
from enum import Enum, unique


@unique
class Stage(Enum):
    """The stage of game which will be a enum type"""
    starting = 0
    judgment = 1
    getCards = 2
    useCards = 3
    discard = 4
    ending = 5
