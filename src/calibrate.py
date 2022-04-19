import time

import cv2
import numpy as np
import pytesseract
from pytesseract import Output

from maze.contrib.ml.camera import Camera
from maze.contrib.ml.colors import ColorDiscriminator

device = Camera.scan(1)

camera = Camera(device, right=False)

t = time.time()
for i in range(1000):
    ret, frame, bf = camera.frame(perspective=True)
    if not ret:
        continue

    # pst1 = np.float32([[95, 89], [230, 37], [250, 404], [98, 375]])
    # pst2 = np.float32([[95, 80], [260, 80], [260, 400], [95, 400]])
    # M = cv2.getPerspectiveTransform(pst1, pst2)
    # rows, cols, dim = frame.shape
    # frame = cv2.warpPerspective(frame, M, (int(cols), int(rows)))
    # # print(M)
    # frame = frame[40:445, 0:310]
    cv2.imshow('p', frame)
    if time.time() - 1 > t:
        l = pytesseract.image_to_string(frame, lang='eng', config='--psm 10 --oem 1 -c tessedit_char_whitelist=hsuHSU', output_type=Output.DICT)
        print(str(l['text'][0]))
        t = time.time()
    cv2.waitKey(1)

# ColorDiscriminator.scan_palette(camera, 10000)
