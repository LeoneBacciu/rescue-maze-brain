from random import randint

from maze.bridge.serial import Serial
from maze.core.communication.envelope import *
from maze.core.utils.constants import *


class Bridge:

    def __init__(self, settings):
        self.settings = settings
        self.serial = Serial(settings.port, settings.baud_rate)

    def handshake(self):
        key = randint(0, 0xff)
        self.serial.write(bytes([START_TOKEN, key, STOP_TOKEN]))
        res = int(self.serial.read()[1])
        if key != res:
            raise Exception(f'{res} different from {key}')

    def send_envelope(self, envelope: BaseOutputEnvelope):
        self.serial.write(bytes(envelope))

    def read_envelope(self):
        return self.settings.input_envelope.from_bytes(self.serial.read())

    def stop(self):
        self.serial.write(b'\xfd\xff')
        del self.serial
