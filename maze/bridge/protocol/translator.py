from maze.core.communication.envelope import *
from maze.core.communication.flags import Flags
from maze.core.errors.errors import *
from maze.core.utils.constants import *


class Translator:

    @staticmethod
    def encode(envelope: Envelope):
        if issubclass(type(envelope.data), Enum):
            direction = [1 if f is envelope.data else 0 for f in list(type(envelope.data))]
        else:
            direction = envelope.data
        flags = []
        if envelope.flags:
            flags = [1 if f in envelope.flags else 0 for f in list(type(envelope.flags[0]))]
        if len(direction) >= BYTE_LIMIT or len(flags) >= BYTE_LIMIT:
            raise EncoderOverflowError
        return bytearray(
            [START_TOKEN] +
            [len(direction), len(flags)] +
            direction + flags +
            [STOP_TOKEN]
        )

    @staticmethod
    def decode(data):

        def toIntArray(array):
            return [int(d) for d in array]

        if data[0] != START_TOKEN or data[-1] != STOP_TOKEN:
            raise MissingDelimitersError
        len_1 = data[1]
        len_2 = len_1 + data[2]
        return Envelope(
            data=toIntArray(data[3:3 + len_1]),
            flags=[Flags.asList[i] for i, f in enumerate(toIntArray(data[3 + len_1:3 + len_2])) if f]
        )
