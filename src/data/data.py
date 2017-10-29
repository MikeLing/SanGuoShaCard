# -*- coding: UTF-8 -*-

from src.models.card import Cards
from src.models.card import Type
from src.models.hero import Hero
from src.util.singleton import Singleton


@Singleton
class Data(object):

    def __init__(self):
        self.heroList = []
        self.cardHeap = []

        self.heroList.append(Hero("曹操", 4, "曹操的技能"))
        self.heroList.append(Hero("刘备", 4, "刘备的技能"))
        self.heroList.append(Hero("诸葛亮", 3, "诸葛亮的技能"))
        self.heroList.append(Hero("曹丕", 4, "曹丕的技能"))
        self.heroList.append(Hero("关羽", 4, "关羽的技能"))
        self.heroList.append(Hero("张飞", 4, "张飞的技能"))

        self.cardHeap.append(Cards("杀", Type.slash, 1))
        self.cardHeap.append(Cards("杀", Type.slash, 2))
        self.cardHeap.append(Cards("杀", Type.slash, 3))
        self.cardHeap.append(Cards("杀", Type.slash, 4))
        self.cardHeap.append(Cards("杀", Type.slash, 5))
        self.cardHeap.append(Cards("杀", Type.slash, 6))
        self.cardHeap.append(Cards("杀", Type.slash, 7))
        self.cardHeap.append(Cards("杀", Type.slash, 8))
        self.cardHeap.append(Cards("杀", Type.slash, 9))
        self.cardHeap.append(Cards("杀", Type.slash, 10))
        self.cardHeap.append(Cards("杀", Type.slash, 11))
        self.cardHeap.append(Cards("闪", Type.dodge, 1))
        self.cardHeap.append(Cards("闪", Type.dodge, 2))
        self.cardHeap.append(Cards("闪", Type.dodge, 3))
        self.cardHeap.append(Cards("闪", Type.dodge, 4))
        self.cardHeap.append(Cards("闪", Type.dodge, 5))
        self.cardHeap.append(Cards("闪", Type.dodge, 6))
        self.cardHeap.append(Cards("闪", Type.dodge, 7))
        self.cardHeap.append(Cards("闪", Type.dodge, 8))
        self.cardHeap.append(Cards("闪", Type.dodge, 9))
        self.cardHeap.append(Cards("闪", Type.dodge, 10))
        self.cardHeap.append(Cards("桃", Type.peach, 1))
        self.cardHeap.append(Cards("桃", Type.peach, 2))
        self.cardHeap.append(Cards("桃", Type.peach, 3))
        self.cardHeap.append(Cards("桃", Type.peach, 4))
        self.cardHeap.append(Cards("桃", Type.peach, 5))
        self.cardHeap.append(Cards("桃", Type.peach, 6))
        self.cardHeap.append(Cards("桃", Type.peach, 7))
    
    def get_heroList(self):
        return self.heroList

    def get_cardHeap(self):
        return self.cardHeap

GAMEDATA = Data.Instance()