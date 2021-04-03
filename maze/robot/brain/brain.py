from abc import ABC, abstractmethod
from copy import copy

from maze.core.communication.envelope import BaseInputEnvelope, BaseOutputEnvelope
from maze.modules.map import AbstractMap
from maze.modules.map.matrix import AbstractCell


class AbstractBrain(ABC):

    def __init__(self, abstract_map: AbstractMap):
        self.map = abstract_map
        self.pos = self.map.pos
        self.prev_pos = copy(self.map.pos)

    @abstractmethod
    def learn(self, envelope: BaseInputEnvelope) -> AbstractCell:
        pass

    @abstractmethod
    def act(self) -> BaseOutputEnvelope:
        pass
