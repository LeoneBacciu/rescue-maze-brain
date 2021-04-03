from maze.contrib.robocup.communication.envelope import InputEnvelope, OutputEnvelope
from maze.contrib.robocup.map.matrix import Cell
from maze.core.communication.directions import Direction
from maze.core.navigation.coord import absolute_to_directions
from maze.robot.brain.brain import AbstractBrain


class Brain(AbstractBrain):
    directions = iter([Direction.top, Direction.top, Direction.left, Direction.top, Direction.top, Direction.right])

    def learn(self, envelope: InputEnvelope) -> Cell:
        return Cell(envelope.walls, black=envelope.black, checkpoint=envelope.checkpoint, victim=False)

    def act(self) -> OutputEnvelope:
        if len(self.buffer) == 0:
            self.buffer = absolute_to_directions(self.map.bfs(lambda c: not c.explored))
        return OutputEnvelope(self.buffer.pop(0), False, False)
