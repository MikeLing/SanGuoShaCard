# -*- coding: UTF-8 -*-

from random import shuffle

from src.data.data import GAMEDATA
from src.util.message import Message

from flask_socketio import emit


class Game(object):
    # players
    players = []
    # watchers
    watchers = []
    # If this game already start
    start = False
    # time for each round of player
    randInterval = 15

    # room id
    room = None

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
            player.setHero(GAMEDATA.get_heroList().pop(-1))
            player.getHero().selected = False
            player.setMaxLifePoint(player.getHero().lifePoint)
            player.setLifePoint(player.getHero().lifePoint)

            # give each player 4 cards
            for i in xrange(4):
                player.getCards().append(Game.availableCards.pop())

            # tell the player what kind of cards he has
            h = player.getHero()
            message = Message("assign")
            message.setData({'cards': [i.title for i in player.getCards()],
                             'hero': [h.name, h.lifePoint, h.skill]})
            emit("init", message.__dict__, room=player.getId())

        # Game started
        Game.currentPlayer = Game.players[0]
        emit("current_player", Game.currentPlayer.getId(), room=Game.room)

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

        emit(Message("end", Game.currentPlayer.getId(), room=Game.room))
