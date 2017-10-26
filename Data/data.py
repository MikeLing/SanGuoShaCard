# -*- coding: UTF-8 -*-

from Models.card import Cards
from Models.card import Type
from Models.hero import Hero

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class Data(object):

    def __init__(self):
        self.heroList = []
        self.cardHeap = []

        self.heroList.append(Hero("曹操"， 4， "曹操的技能"))
        self.heroList.append(Hero("刘备"， 4， "刘备的技能"))
        self.heroList.append(Hero("诸葛亮"， 3， "诸葛亮的技能"))
        self.heroList.append(Hero("曹丕"， 4， "曹丕的技能"))
        self.heroList.append(Hero("关羽"， 4， "关羽的技能"))
        self.heroList.append(Hero("张飞"， 4， "张飞的技能"))

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