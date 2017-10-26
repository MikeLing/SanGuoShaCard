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
            self.start = True
            PlayersId = []
            for player in self.players:
                PlayersId.append(player.getId())