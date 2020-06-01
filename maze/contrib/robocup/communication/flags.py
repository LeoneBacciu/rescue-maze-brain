from enum import Enum, auto


class Flags(Enum):
    WasRamp = auto()
    WasBlack = auto()
    IsCheckpoint = auto()
    NotNew = auto()
    Climb = auto()

