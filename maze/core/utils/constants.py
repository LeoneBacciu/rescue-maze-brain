from enum import Enum, auto

NEIGHBOURS = ((1, 0), (0, 1), (-1, 0), (0, -1))

"""Serial constants"""
BYTE_LIMIT = 0xdf
START_TOKEN = 0xfe
STOP_TOKEN = 0xff


class Directions(Enum):
    RIGHT = auto()
    UP = auto()
    LEFT = auto()
    DOWN = auto()

