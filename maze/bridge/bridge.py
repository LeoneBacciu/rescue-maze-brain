from random import randint
from typing import Optional

from maze.bridge.serial import Serial
from maze.core.communication.directions import Direction
from maze.core.communication.envelope import *
from maze.core.errors.errors import HandshakeException
from maze.core.utils.constants import *


class Bridge:

    def __init__(self, settings):
        self.settings = settings
        self.serial = Serial(settings.port, settings.baud_rate)

    def flush(self):
        self.serial.flush()

    def handshake(self):
        key = randint(0, 0xfb)
        self.serial.write(bytes([START_TOKEN, key, STOP_TOKEN]))
        data = self.serial.read()
        print(data)
        res = int(data[1])
        if key != res:
            raise Exception(f'{res} different from {key}')

    def receive_handshake(self):
        try:
            return int(self.serial.read()[1])
        except HandshakeException as e:
            return int(e.value[1])

    def send_handshake(self, v):
        self.serial.write(bytes([HANDSHAKE_TOKEN, v, STOP_TOKEN]))

    def send_envelope(self, envelope: BaseOutputEnvelope):
        self.serial.write(bytes(envelope))

    def read_envelope(self):
        return self.settings.input_envelope.from_bytes(self.serial.read())

    def send_halfway_envelope(self, envelope: BaseHalfwayEnvelope):
        self.serial.write(bytes(envelope))

    def read_halfway_envelope(self):
        return self.settings.input_halfway_envelope.from_bytes(self.serial.read())

    def stop(self):
        self.serial.write(b'\xfe\xff')
        del self.serial
