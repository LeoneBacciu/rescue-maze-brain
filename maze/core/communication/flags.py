from enum import Enum, auto


class BaseFlags(Enum):
    WasRamp = auto()

    NotNew = auto()
    Climb = auto()

    @staticmethod
    def ordered():
        return Enum('Flags', " ".join([f.value for f in BaseFlags]))

    @staticmethod
    def extend(name: str, fields: str):
        return Enum(name, f'{" ".join([f.value for f in BaseFlags])} {fields.strip()}')


Flags = BaseFlags.ordered()
setattr(Flags, "asList", list(Flags))
