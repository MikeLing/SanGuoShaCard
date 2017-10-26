from autobahn.twisted.websocket import WebSocketClientProtocol
from GameTable.gameServer import GAMESERVER
from Util.message import Message

class PlayerClient(WebSocketClientProtocol):
    def __init__(self, id):
        self._id = id
        self._player = None

    def setPlayer(self, player):
        self._player = player

    def getPlayer(self):
        return self._player

    def getId(self):
        return self._id
    
    def onOpen(self):
        GAMESERVER.addConnections(self)
        player = new player(id, self)
        Game.addConnections(player)

        # new connection
        loginMessage = Message()
        loginMessage.setAction("login")
        loginMessage.setData(self.getId())

        sendSelf(loginMessage)

        newMessage = Message()
        newMessage.setAction("new_login")
        newMessage.setData(self.getId())
        GAMESERVER.broadcast(newMessage)
    
    def onClose(self):
        leaveMessage = Message()
        leaveMessage.setAction("logout")
        leaveMessage.setData(self.getId())
        GAMESERVER.broadcast(leaveMessage)

        if Game.starting and player in Game.getPlayer()

