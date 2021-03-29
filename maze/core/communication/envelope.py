from maze.core.utils.constants import *


class BaseInputEnvelope:

    def __init__(self, walls, *flags):
        self.walls = walls

    @classmethod
    def from_bytes(cls, data):
        walls = [bool(w) for w in data[1:5]]
        flags = map(lambda f: f == 0x01, data[5:-1])
        return cls(walls, *flags)


class BaseOutputEnvelope:

    def __init__(self, direction, *flags):
        self.direction = direction

    def __bytes__(self):
        direction = [0] * 4
        direction[self.direction.value] = 1
        flags = [int(v) for f, v in vars(self).items() if f != 'direction' and isinstance(v, bool)]
        return bytes([START_TOKEN] + direction + flags + [STOP_TOKEN])