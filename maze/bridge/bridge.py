from maze.core.communication.envelope import *
from maze.core.utils.settings import SerialSettings
from maze.bridge.protocol import Translator
from maze.bridge.serial import Serial


class Bridge:

    def __init__(self, settings: SerialSettings):
        self.settings = settings
        self.serial = Serial(settings.port, settings.baud_rate)

    def send(self, direction, flags):
        self.sendEnvelope(Envelope(data=direction, flags=flags))

    def sendEnvelope(self, envelope: Envelope):
        self.serial.send(Translator.encode(envelope))

    def read(self):
        return self.readEnvelope().split()

    def readEnvelope(self):
        return Translator.decode(self.serial.waitAndRead())
