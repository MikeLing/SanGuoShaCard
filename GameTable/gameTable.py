from Data.data import Data
from random import shuffle
from GameTable.gameServer import Server
from Util.message import Message

class Game(object):
    # players
    players = []
    # watchers
    watchers = []
    # If this game already start
    start = False
    # time for each round of player
    randInterval = 15
    # room name
    name = "一号桌"
    # available card heap
    availableCards = []

    # discard card heap
    discardCards = []

    # current player
    currentPlayer = None

    # game action
    actions = []

    @staticmethod
    def init_game_table():
        # init all the cards and hero
        Game.start = True
        PlayersId = []

        # init player slot
        for player in Game.players:
            PlayersId.append(player.getId())

        # init card heap
        Game.availableCards = GAMEDATA.get_cardHeap()
        shuffle(Game.availableCards)

        # init player
        for player in Game.players:
            player.setMaxLifePoint(player.getHero().lifePoint)
            player.setLifePoint(player.getHero().lifePoint)

            # give each player 4 cards
            for i in xrange(4):
                player.getCards().append(Game.availableCards.pop())
            
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
        Game.currentPlayer = Game.players[0]
        Game.actions.add(new CardAction(Game.currentPlayer))
        Server.broadcast(Message("begining", Game.currentPlayer.getId()))

    @staticmethod
    def end():
        Game.start = False
        Game.currentPlayer = None

        Game.availableCards = []
        Game.discardCards = []

        Game.actions = []

        # reset all the heros
        for hero in GAMEDATA.get_heroList():
            hero.selected = False

        # reset all the player
        for p in Game.players:
            p.setCards([])
            p.setGeneral(None)

        Server.broadcast(Message("ending"));
