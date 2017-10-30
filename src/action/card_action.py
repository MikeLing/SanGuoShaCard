import json

from src.models.card import Cards
from src.data.data import GAMEDATA
from src.models.card import Type
from src.game_table.game import Game
from src.game_table.player import Player
from src.util.message import Message
from src.action.slash_action import SlashAction

from flask_socketio import emit


class CardAction(object):

    def __init__(self, player):
        self.player = player

    def execute(self, sender, packet):
        cards = GAMEDATA.get_cardHeap()
        jsonData = json.loads(packet.decode('utf8'))
        if sender.equals(self.player):
            action = jsonData["action"]

        if action == "game_card":
            cardId = jsonData["card"]
            card = cards.get(cardId)

            if card in self.player.getCards():
                targetId = None

                if card.type == Type.slash:
                    targetId = jsonData["target"]
                    target = Game.players.get(
                        Game.players.indexOf(Player(targetId, None)))
                    Game.actions.add(SlashAction(self.player, target))

                if card.type == Type.peach:
                    if self.player.getLifePoint() < self.player.getMaxLifePoint():
                        self.player.setLifePoint(
                            self.player.getLifePoint() + 1)
                    message = Message("game_health")
                    message.addData("player", self.player.getId())
                    message.addData("health", self.player.getHealth())
                    emit('peach_action', message, room=jsonData['room'])

                self.player.getCards().remove(cardId)
                Game.discards.append(card)

                message = Message("game_card")
                message.addData("card", cardId)
                message.addData("player", self.player.getId())
                message.addData("target", targetId)
                emit('update', message, room=jsonData['room'])

            else:
                self.player.sendSelf(
                    Message("system_info", "You have not this card"))

        elif action == "game_discard":
            Game.actions.remove(self)
            index = Game.players.indexOf(self.player)
            index = (index + 1) % Game.players.size()
            nextPlayer = Game.players.get(index)

            Game.actions.add(CardAction(nextPlayer))

            msgList = []
            msgList.append(Message("discard", sender.getId()))
            msgList.append(Message("begining", nextPlayer.getId()))

            emit('update', message, room=jsonData['room'])

    def getPlayer(self):
        return self.player
