from Data.data import Data
from random import shuffle
from GameTable.gameServer import GAMESERVER
from Util.message import Message

class Game(object):

    def __init__(self):
        # players
        self.players = []
        # watchers
        self.watchers = []
        # If this game already start
        self.start = False
        # time for each round of player
        self.randInterval = 15
        # room name
        self.name = "一号桌"
        # available card heap
        self.availableCards = []

        # discard card heap
        self.discardCards = []

        # current player
        self.currentPlayer = None

        # game action
        self.actions = []

    def init_game_table(self):
        # init all the cards and hero
        self.start = True
        PlayersId = []

        # init player slot
        for player in self.players:
            PlayersId.append(player.getId())

        # init card heap
        self.availableCards = GAMEDATA.get_cardHeap()
        shuffle(self.availableCards)

        # init player
        for player in self.players:
            player.setMaxLifePoint(player.getHero().lifePoint)
            player.setLifePoint(player.getHero().lifePoint)

            # give each player 4 cards
            for i in xrange(4):
                player.getCards().append(self.availableCards.pop())
            
            startMessage = Message()
            startMessage.setAction("start")
            startMessage.addData("id", player.getId())
            startMessage.addData("count", 4)
            player.broadcastIgnoreSelf(startMessage)

            # send to itself
            selfMessage = Message()
            selfMessage.setAction("start")
            selfMessage.addData("id", player.getId())

            # To tell the user what kind of card he has
            haveCards = [Data.Cards.indexOf(c) for c in player.getCards()]
            selfMessage.addData("cards", haveCards)
            selfMessage.addData("players", playersId)
            player.sendSelf(selfMessage)
        
        # Game started
        self.currentPlayer = players[0]
        self.actions.add(new CardAction(currentPlayer))
        GAMESERVER.broadcast(Message("begining", currentPlayer.getId()))


    def end(self):
        self.start = False
        self.currentPlayer = None

        self.availableCards = []
        self.discardCards = []

        self.actions = []

        # reset all the heros
        for hero in GAMEDATA.get_heroList():
            hero.selected = False

        # reset all the player
        for p in self.players:
            p.setCards([])
            p.setGeneral(None)

        Server.broadcast(Message("ending"));
