import json

from Models.card import Cards
from Data.data import GAMEDATA
from Models.card import Type
from GameTable.game import Game
from GameTable.player import Player
from GameTable.gameServer import Server
from Util.message import Message
from Action.slashAction import SlashAction


class SlashAction(object):

    def __init__(self, p, t):
        self.player = p
        self.target = t
    
    def getPlayer(self):
        return self.player

    def getTarget(self):
        return self.target

    def execute(sender, packet):
        cards = GAMEDATA.get_cardHeap()
        jsonData = json.loads(packet.decode('utf8'))
        if sender == self.target:
            action = jsonData["action"]

            if action == "game_card":
                cardId = jsonData["card"]
                card = cards.get(cardId)

                if card in self.player.getCards():
                    if card.type == Type.dodge:
                        self.target.getCards().remove(cardId)
                        Game.actions.remove(self)
                        message = Message("game_card")
                        message.addData("card", cardId)
                        message.addData("player", self.target.getId())
                        Server.broadcast(message)
                    else:
                        target.sendSelf(Message("message", "Wrong card"))
                else:
                    target.sendSelf(Message("message", "You have not this card"))
            elif action == "game_cancel":
                target.setHealth(target.getHealth() - 1)
                Game.actions.remove(self)

                Server.broadcast(Message("game_health")
                addData("player", target.getId())
                addData("health", target.getHealth())
        
        else:
            sender.sendSelf(Message("message", "It is not your turn"));