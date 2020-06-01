from maze.core.utils.settings import MazeSettings, SerialSettings
from maze.robot.brain.brain import AbstractBrain


class Robot:

    def __init__(self, maze_settings: MazeSettings, serial_settings: SerialSettings):
        self.map = maze_settings.map(maze_settings)
        self.bridge = serial_settings.bridge(serial_settings)
        self.brain = AbstractBrain(self.map, serial_settings)

    def run(self):
        while True:
            data, flags = self.bridge.read()
            print(data, flags)
            data, flags = self.brain.act(data, flags)
            self.bridge.send(data, flags)
