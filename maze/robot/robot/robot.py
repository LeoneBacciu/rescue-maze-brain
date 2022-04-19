from typing import Type

from maze.contrib.robocup.robot.brain import Brain
from maze.core.errors.errors import StopExecution, HandshakeException
from maze.core.utils.settings import MazeSettings, SerialSettings


class Robot:

    def __init__(self, brain: Type[Brain], maze_settings: MazeSettings, serial_settings: SerialSettings):
        self.map = maze_settings.map(maze_settings)
        self.bridge = serial_settings.bridge(serial_settings)
        self.brain = brain(self.map)

    def single_run(self):
        while True:
            ie = self.bridge.read_envelope()
            print(ie)

            if not self.map.current_cell.explored:
                self.map.update(self.brain.learn(ie))

            if not self.brain.successful(ie):
                self.map.rollback()

            self.map.print()

            oe = self.brain.act(ie)
            print(oe)

            self.map.goto(oe.direction)
            self.bridge.send_envelope(oe)

            hie = self.bridge.read_halfway_envelope()
            print(hie)
            hoe = self.brain.halfway(oe.ignore, hie)
            print(hoe)
            self.bridge.send_halfway_envelope(hoe)

    def run(self):
        # self.bridge.flush()
        # self.bridge.handshake()
        hs = self.bridge.receive_handshake()
        print(f'handshake {hex(hs)}')
        self.bridge.send_handshake(hs)

        while True:
            try:
                self.single_run()
            except StopExecution:
                break
            except HandshakeException as e:
                self.brain.resume()
                self.bridge.send_handshake(e.value[1])

        self.bridge.stop()
        return
