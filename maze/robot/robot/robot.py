from typing import Type

from maze.contrib.robocup.robot.brain import Brain
from maze.core.utils.settings import MazeSettings, SerialSettings


class Robot:

    def __init__(self, brain: Type[Brain], maze_settings: MazeSettings, serial_settings: SerialSettings):
        self.map = maze_settings.map(maze_settings)
        self.bridge = serial_settings.bridge(serial_settings)
        self.brain = brain(self.map)

    def run(self):
        self.bridge.handshake()
        prev_direction = None
        while True:
            ie = self.bridge.read_envelope()

            if prev_direction and self.brain.successful(ie):
                self.map.goto(prev_direction)

            self.map.update(self.brain.learn(ie))
            try:
                oe = self.brain.act()
            except StopIteration:
                break
            prev_direction = oe.direction
            self.bridge.send_envelope(oe)
        self.bridge.stop()
        return
        # while True:
        #     data, flags = self.bridge.read()
        #     print(data, flags)
        #     data, flags = self.brain.act(data, flags)
        #     self.bridge.write(data, flags)
