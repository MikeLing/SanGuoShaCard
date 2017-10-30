import json

from src.models.card import Cards
from src.data.data import GAMEDATA
from src.models.card import Type
from src.game_table.game import Game
from src.game_table.player import Player
from src.util.message import Message
from flask_socketio import emit


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
                        emit('slash_action', message, room=jsonData['room'])
                    else:
                        emit('warning', "Wrong card", room=jsonData['room'])
                else:
                    emit('warning', "You don't have that card", room=sender)
            elif action == "game_cancel":
                self.target.setHealth(self.target.getHealth() - 1)
                Game.actions.remove(self)
        else:
            emit('warning', "It's not your turn", room=sender)
