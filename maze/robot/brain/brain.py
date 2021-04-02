from abc import ABC, abstractmethod
from copy import copy
from typing import Type

from maze.core.communication.envelope import BaseInputEnvelope, BaseOutputEnvelope
from maze.modules.map import AbstractMap
from maze.modules.map.matrix import AbstractCell


class AbstractBrain(ABC):

    def __init__(self, abstract_map: AbstractMap, input_envelope: Type[BaseInputEnvelope],
                 output_envelope: Type[BaseOutputEnvelope]):
        self.map = abstract_map
        self.pos = self.map.pos
        self.prev_pos = copy(self.map.pos)
        self.in_flag = input_envelope
        self.out_flags = output_envelope

    @abstractmethod
    def learn(self, envelope: BaseInputEnvelope) -> AbstractCell:
        pass

    @abstractmethod
    def act(self, walls, flags: BaseOutputEnvelope):
        pass
