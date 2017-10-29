"""
    This module is the definiation of client online
"""


class Client():
    def __init__(self, id):
        self.id = id
        self.player = None

    def setPlayer(self, player):
        self.player = player

    def getPlayer(self):
        return self.player

    def getId(self):
        return self.id
    