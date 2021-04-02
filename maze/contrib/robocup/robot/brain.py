from maze.contrib.robocup.communication.envelope import InputEnvelope
from maze.contrib.robocup.map.matrix import Cell
from maze.robot.brain.brain import AbstractBrain


class Brain(AbstractBrain):

    def learn(self, envelope: InputEnvelope) -> Cell:
        return Cell(envelope.walls, black=envelope.black, checkpoint=envelope.checkpoint, victim=False)

    def act(self, data, flags):
        pass
        return [0] * 4, []
