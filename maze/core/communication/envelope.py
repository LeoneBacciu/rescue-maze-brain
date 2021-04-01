from abc import ABC, abstractmethod

from maze.core.utils.constants import *


class BaseInputEnvelope(ABC):

    @abstractmethod
    def __init__(self, walls, *flags):
        self.walls = walls

    @classmethod
    def from_bytes(cls, data):
        walls = [bool(w) for w in data[1:5]]
        return cls(walls, *data[5:-1])

    def __str__(self):
        flags = {k: v for k, v in vars(self).items() if k != 'walls'}
        return f'Walls: {str(self.walls)}, Flags: {str(flags)}'


class BaseOutputEnvelope(ABC):

    @abstractmethod
    def __init__(self, direction, *flags):
        self.direction = direction

    def __bytes__(self):
        direction = [0] * 4
        direction[self.direction.value] = 1
        flags = [v for f, v in vars(self).items() if f != 'direction' and isinstance(v, int)]
        return bytes([START_TOKEN] + direction + flags + [STOP_TOKEN])

    def __str__(self):
        flags = {k: v for k, v in vars(self).items() if k != 'direction'}
        return f'Direction: {str(self.direction)}, Flags: {str(flags)}'
