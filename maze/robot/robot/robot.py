from typing import Type

from maze.contrib.robocup.robot.brain import Brain
from maze.core.errors.errors import StopExecution
from maze.core.utils.settings import MazeSettings, SerialSettings


class Robot:

    def __init__(self, brain: Type[Brain], maze_settings: MazeSettings, serial_settings: SerialSettings):
        self.map = maze_settings.map(maze_settings)
        self.bridge = serial_settings.bridge(serial_settings)
        self.brain = brain(self.map)

    def run(self):
        self.bridge.handshake()
        print("handshake")
        while True:
            ie = self.bridge.read_envelope()
            print(ie)

            if not self.map.current_cell.explored:
                self.map.update(self.brain.learn(ie))

            if not self.brain.successful(ie):
                self.map.rollback()

            try:
                oe = self.brain.act()
            except StopExecution:
                break
            self.map.goto(oe.direction)
            print(oe)
            self.bridge.send_envelope(oe)
            if self.bridge.read_halfway_point() != 0:
                self.brain.halfway()
            else:
                print("no halfway")
        self.bridge.stop()
        return
