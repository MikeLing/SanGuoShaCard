from autobahn.twisted.websocket import WebSocketClientProtocol
from GameTable.gameServer import Server
from Util.message import Message
from GameTable.gameTable import Game
from GameTable.player import Player

class PlayerClient(WebSocketClientProtocol):
    def __init__(self, id):
        self.id = id
        self.player = None

    def setPlayer(self, player):
        self.player = player

    def getPlayer(self):
        return self.player

    def getId(self):
        return self.id
    
    def onOpen(self):
        Server.addConnections(self)
        self.player = Player(id, self)
        Game.addConnections(self.player)

        # new connection
        loginMessage = Message()
        loginMessage.setAction("login")
        loginMessage.setData(self.getId())

        self.sendMessage(loginMessage)

        newMessage = Message()
        newMessage.setAction("new_login")
        newMessage.setData(self.getId())
        Server.broadcast(newMessage)
    
    def onClose(self):
        leaveMessage = Message()
        leaveMessage.setAction("logout")
        leaveMessage.setData(self.getId())
        Server.broadcast(leaveMessage)

        if Game.start and self.player in Game.players:
            Game.end()

        if self.player != None and self.player.getHero() != None:
            self.player.getHero().setSelected(False)

        Game.players.remove(self.player)

        Server.connections.remove(self)

    def onMessage(self, payload, isBinary):
        data = payload.decode('utf8')
        action = data["action"]
        if action == "message":
            me = Message()
            me.setAction("message")
            me.addData("id", id)
            me.addData("message", data["message"])

            Server.broadcast(me)
        
        elif action == "init":
            me = Message()
            me.setAction("init")
            players = []
            for p in Game.players:
                temp = {}
                temp['id'] = p.getId()
                players.append(temp)
            me.setData(players)
            self.sendMessage(me)
        elif action == "start":
            Game.init_game_table()

        elif action.startsWith("game_"):
            Game.actions.get(Game.actions.size()-1).execute(self.player, data)