# set PYTHONPATH=%PYTHONPATH%;C:\Users\sonoa\PyCharmProjects\rescue-maze-brain\
# export PYTHONPATH="${PYTHONPATH}:/home/pi/robot/rescue-maze-brain/"
import os
import time

import cv2
import numpy as np

from maze.contrib.ml.camera import Camera
from maze.contrib.ml.analysis import read_all
from maze.contrib.robocup.communication.envelope import InputEnvelope, OutputEnvelope, InputHalfwayEnvelope, \
    OutputHalfwayEnvelope
from maze.contrib.robocup.map import Map
from maze.core.utils.settings import *
from maze.bridge import Bridge
from maze.robot.robot.robot import Robot
from maze.contrib.robocup.robot.brain import Brain

if __name__ == '__main__':

    # import serial
    #
    # s = serial.Serial('/dev/ttyUSB0', 115200, timeout=None)
    # s.write(b'\xfd\x04\xff')
    # print(s.in_waiting)
    #
    # exit(0)
    # c1 = Camera(0)
    # c2 = Camera(2)

    # load_loop('/home/stark/PycharmProjects/rescue-maze-brain/data')
    # train('/home/stark/PycharmProjects/rescue-maze-brain/data')
    # cd = ColorDiscriminator([np.array([65, 120, 20]), np.array([5, 10, 85]), np.array([50, 135, 175])],
    #                         ['green', 'red', 'yellow'])

    # for i in range(100):
    #     print('l')
    #     read_color_and_letter(l_camera)
    #     print('r')
    #     read_color_and_letter(l_camera)
    #     time.sleep(.1)
    # while not Brain.l_camera.frame()[0]:
    #     print(Brain.l_camera.frame())
    #     time.sleep(1)
    #
    # ColorDiscriminator.scan_palette(Brain.r_camera, 10000)
    # for i in range(5):
        # r, f, bf = Brain.r_camera.frame()
        # if not r:
        #     continue
        # cv2.imshow('p', f)
        # left = read_color_and_letter(Brain.l_camera)
        # right = read_color_and_letter(Brain.r_camera)
        # print(left)
        # print(right)
        # cv2.waitKey(1)
    # c = Camera(0)
    # print(c)
    # while True:
    #     print(read_all(Brain.l_camera))
    #     print(read_all(Brain.r_camera, debug=True))
        # print()
        # time.sleep(0.2)
    # exit(0)

    maze_settings = MazeSettings(
        map=Map,
        matrix=Matrix,
        cell=Cell,
        dims=(1, 12, 12)
    )

    serial_settings = SerialSettings(
        bridge=Bridge,
        port='/dev/ttyUSB0',
        # port='/dev/ttyS0',
        baud_rate=115200,
        input_envelope=InputEnvelope,
        output_envelope=OutputEnvelope,
        input_halfway_envelope=InputHalfwayEnvelope,
        output_halfway_envelope=OutputHalfwayEnvelope,
    )

    robot = Robot(
        brain=Brain,
        maze_settings=maze_settings,
        serial_settings=serial_settings
    )

    input('waiting...')

    robot.run()
