import time
from typing import Optional, Tuple

from maze.contrib.ml.analysis import read_all
from maze.contrib.ml.camera import Camera
from maze.contrib.robocup.communication.envelope import InputEnvelope, OutputEnvelope, InputHalfwayEnvelope, \
    OutputHalfwayEnvelope
from maze.contrib.robocup.map.matrix import Cell
from maze.core.communication.directions import Direction
from maze.core.communication.envelope import BaseHalfwayEnvelope
from maze.core.errors.errors import NoCellsMatch, StopExecution
from maze.core.navigation.coord import absolute_to_directions
from maze.robot.brain.brain import AbstractBrain


class Brain(AbstractBrain):
    end = False
    first = True
    # busses = Camera.list_cameras()
    l_camera = Camera(0, right=False)
    r_camera = Camera(2, right=True)

    def successful(self, envelope: InputEnvelope) -> bool:
        return not envelope.black

    def learn(self, envelope: InputEnvelope) -> Cell:
        if envelope.black:
            return Cell([True] * 4, black=envelope.black, checkpoint=False, victim=False)
        return Cell(envelope.walls, black=envelope.black, checkpoint=envelope.checkpoint, victim=False)

    def halfway(self, ignore: bool, he: InputHalfwayEnvelope) -> OutputHalfwayEnvelope:
        print(f'halfway ({ignore}) ({str(he)})')
        if not ignore:
            q = self.read_walls(he.sides)
            print(f'drop: {hex(q)}')
            return OutputHalfwayEnvelope(drop=q)
        return OutputHalfwayEnvelope(drop=0x00)

    def act(self, envelope: InputEnvelope) -> OutputEnvelope:
        drop = 0
        if len(self.buffer) == 0:
            try:
                print('end check')
                if self.first:
                    self.first = False

                if not self.first and not envelope.black:
                    drop = self.read_walls(envelope.sides)
                print(f'drop: {hex(drop)}')

                self.buffer = absolute_to_directions(self.map.bfs(lambda c: not c.explored))
            except NoCellsMatch:
                if not self.end:
                    print('go home')
                    self.buffer = absolute_to_directions(self.map.go_home())
                    self.end = True
                else:
                    raise StopExecution()

        return OutputEnvelope(self.buffer.pop(0), len(self.buffer) > 0, drop)

    def read_walls(self, sides):
        time.sleep(.5)
        out = 0
        if (sides >> 4) > 0:
            letter, color = read_all(self.l_camera)
            print(f'L: letter({letter}) color({color})')
            out += {'': 0, 'g': 1, 'y': 2, 'r': 2}[color]
            if out == 0:
                out += {'': 0, 'u': 1, 's': 3, 'h': 4}[letter]
            if out > 0:
                return out << 4

        if (sides & 0xf) > 0:
            letter, color = read_all(self.r_camera)
            print(f'R: letter({letter}) color({color})')
            out += {'': 0, 'g': 1, 'y': 2, 'r': 2}[color]
            if out == 0:
                out += {'': 0, 'u': 1, 's': 3, 'h': 4}[letter]
            if out > 0:
                return out
        return 0

    def resume(self):
        point = self.map.last_checkpoint
        self.map.teleport(point.coord)
        self.buffer.clear()
