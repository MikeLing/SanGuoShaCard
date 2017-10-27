"""
    A model to represent hero in the game
"""

class Hero(object):
    """A class represent hero in the game"""
    def __init__(self, name, lifePoint, skills):
        self._name = name
        self._lifePoint = lifePoint
        self._skill = skills
        self._selected = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = newName

    @property
    def lifePoint(self):
        return self._lifePoint

    @lifePoint.setter
    def lifePoint(self, newLifePoint):
        self.lifePoint = newLifePoint

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, sk):
        self._skill = sk

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, isSelected):
        self._selected = isSelected

