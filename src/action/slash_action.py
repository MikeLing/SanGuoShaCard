import json

from models.card import Cards
from data.data import GAMEDATA
from models.card import Type
from game_table.game import Game
from game_table.player import Player
from game_table.server import Server
from util.message import Message
from action.slashAction import SlashAction


class SlashAction(object):

    def __init__(self, p, t):
        self.player = p
        self.target = t
    
    def getPlayer(self):
        return self.player

    def getTarget(self):
        return self.target

    def execute(self, sender, packet):
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
                        self.target.sendSelf(Message("message", "Wrong card"))
                else:
                    self.target.sendSelf(Message("message", "You have not this card"))
            elif action == "game_cancel":
                self.target.setHealth(self.target.getHealth() - 1)
                Game.actions.remove(self)
        else:
            sender.sendSelf(Message("message", "It is not your turn"));