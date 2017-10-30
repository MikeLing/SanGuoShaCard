"""
Defination of game player
"""

import json


class Player(object):

    def __init__(self, id):
        self.id = id

        self.lifePoint = 0
        self.maxLifePoint = 0

        # Hero
        self.hero = None

        # weapon card
        self.waepon = None
        self.armor = None
        self.plus = None
        self.minus = None
        self.cards = []

        # game rule (The card can reach other player or not)
        self.supplyShortage = None
        self.indulgence = None

    def __eq__(self, other):
        return (self.id == other.id and self.hero == other.hero)

    def getId(self):
        return self.id

    def getMaxLifePoint(self):
        return self.maxLifePoint

    def setMaxLifePoint(self, mLifePoint):
        self.maxLifePoint = mLifePoint

    def getSupplyShortage(self):
        return self.supplyShortage

    def setSupplyShortage(self, sShortage):
        self.supplyShortage = sShortage

    def getIndulgence(self):
        return self.supplyShortage

    def setIndulgence(self, indulgence):
        self.indulgence = indulgence

    def getHero(self):
        return self.hero

    def setHero(self, hero):
        self.hero = hero
        self.maxLifePoint = hero.lifePoint
        self.lifePoint = hero.lifePoint

    def getLifePoint(self):
        return self.lifePoint

    def setLifePoint(self, lPoint):
        self.lifePoint = lPoint

    def getWeapon(self):
        return self.waepon

    def setWeapon(self, weapon):
        self.waepon = weapon

    def getArmor(self):
        return self.armor

    def setArmor(self, armor):
        self.armor = armor

    def getPlus(self):
        return self.plus

    def setPlus(self, plus):
        self.plus = plus

    def getMinus(self):
        return self.minus

    def setMinus(self, minus):
        self.minus = minus

    def getCards(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards
