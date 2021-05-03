from random import randint
from typing import Optional

from maze.contrib.robocup.communication.envelope import InputEnvelope, OutputEnvelope
from maze.contrib.robocup.map.matrix import Cell
from maze.core.communication.directions import Direction
from maze.core.errors.errors import NoCellsMatch, StopExecution
from maze.core.navigation.coord import absolute_to_directions
from maze.robot.brain.brain import AbstractBrain


class Brain(AbstractBrain):

    def successful(self, envelope: InputEnvelope) -> bool:
        return not envelope.black

    def learn(self, envelope: InputEnvelope) -> Cell:
        if envelope.black:
            return Cell([True] * 4, black=envelope.black, checkpoint=False, victim=False)
        return Cell(envelope.walls, black=envelope.black, checkpoint=envelope.checkpoint, victim=False)

    def halfway(self) -> Optional[Direction]:
        # TODO: check visual victims
        return

    def act(self) -> OutputEnvelope:
        if len(self.buffer) == 0:
            try:
                self.buffer = absolute_to_directions(self.map.bfs(lambda c: not c.explored))
            except NoCellsMatch:
                raise StopExecution()
        n = randint(0, 10)
        if n == 0:
            n = 0x01
        elif n == 1:
            n = 0x10
        else:
            n = 0
        return OutputEnvelope(self.buffer.pop(0), len(self.buffer) > 0, 0)
