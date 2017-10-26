"""
    A model to represent hero in the game
"""

class Hero(object):
    """A class represent hero in the game"""
    def __init__(self, name, health, skills):
        self._name = name
        self._health = health
        self._skill = skills

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = newName

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, newHealth):
        self.health = newHealth

