from abc import ABC, abstractmethod

from maze.modules.map import AbstractMap
from copy import copy


class AbstractBrain(ABC):

    def __init__(self, abstract_map: AbstractMap, flag):
        self.map = abstract_map
        self.pos = self.map.pos
        self.prev_pos = copy(self.map.pos)
        self.flag = flag

    @abstractmethod
    def act(self, data, flags):
        pass
