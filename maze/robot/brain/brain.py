from abc import ABC, abstractmethod
from typing import Optional

from maze.core.communication.directions import Direction
from maze.core.communication.envelope import BaseInputEnvelope, BaseOutputEnvelope
from maze.modules.map import AbstractMap
from maze.modules.map.matrix import AbstractCell


class AbstractBrain(ABC):

    def __init__(self, abstract_map: AbstractMap):
        self.map = abstract_map
        self.buffer = []

    @abstractmethod
    def successful(self, envelope: BaseInputEnvelope) -> bool:
        pass

    @abstractmethod
    def learn(self, envelope: BaseInputEnvelope) -> AbstractCell:
        pass

    @abstractmethod
    def halfway(self) -> Optional[Direction]:
        pass

    @abstractmethod
    def act(self) -> BaseOutputEnvelope:
        pass
