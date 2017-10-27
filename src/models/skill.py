"""
    This model is about the skill of hero.
"""

class Skill(object):
    """Hero skill"""
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        """
            getter for skill name
        """
        return self._name
