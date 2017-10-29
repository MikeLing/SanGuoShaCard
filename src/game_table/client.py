from autobahn.twisted.websocket import WebSocketClientProtocol
from src.game_table.server import Server
from src.util.message import Message
from src.game_table.game import Game
from src.game_table.player import Player

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
    