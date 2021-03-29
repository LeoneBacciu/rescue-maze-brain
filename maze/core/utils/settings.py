from typing import Type

from maze.bridge import Bridge
from maze.contrib.robocup.map import Map
from maze.contrib.robocup.map.matrix import Matrix, Cell, Walls
from maze.core.communication.envelope import BaseInputEnvelope, BaseOutputEnvelope


class MazeSettings:

    def __init__(self, map: Type[Map], matrix: Type[Matrix], cell: Type[Cell], walls: Type[Walls], dims, backup=False,
                 backup_dir='./backup'):
        self.map = map
        self.matrix = matrix
        self.cell = cell
        self.walls = walls
        self.dims = dims
        self.backup = backup
        self.backup_dir = backup_dir


class SerialSettings:

    def __init__(self, bridge: Type[Bridge], port: str, baud_rate: int, input_envelope: Type[BaseInputEnvelope],
                 output_envelope: Type[BaseOutputEnvelope]):
        self.bridge = bridge
        self.port = port
        self.baud_rate = baud_rate
        self.input_envelope = input_envelope
        self.output_envelope = output_envelope
