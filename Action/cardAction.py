import json

from Models.card import Cards
from Data.data import GAMEDATA
from Models.card import Type
from GameTable.game import Game
from GameTable.player import Player
from GameTable.gameServer import Server
from Util.message import Message
from Action.slashAction import SlashAction

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
                    target = Game.players.get(Game.players.indexOf(Player(targetId, None)))
                    Game.actions.add(SlashAction(self.player, target))
                
                if card.type == Type.peach:
                    if self.player.getLifePoint() < self.player.getMaxLifePoint():
                        self.player.setLifePoint(self.player.getLifePoint() + 1)
                    message = Message("game_health")
                    message.addData("player", self.player.getId())
                    message.addData("health", self.player.getHealth())
                    Server.broadcast(message)
            
                self.player.getCards().remove(cardId)
                Game.discards.append(card)

                message = Message("game_card")
                message.addData("card", cardId)
                message.addData("player", self.player.getId())
                message.addData("target", targetId)
                Server.broadcast(message)

            else:
                self.player.sendSelf(Message("system_info", "You have not this card"))

        elif action == "game_card":
            Game.actions.remove(self)
            index = Game.players.indexOf(self.player)
            index = (index + 1) % Game.players.size()
            nextPlayer = Game.players.get(index)

            Game.actions.add(new CardAction(nextPlayer))


            msgList = []
            msgList.append(Message("discard", sender.getId()))
            msgList.append(Message("begining", nextPlayer.getId()))

            Server.broadcast(msgList)

    def getPlayer(self):
        return self.player
