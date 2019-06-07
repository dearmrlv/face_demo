from frame import Frame
import cv2
from imtools import get_group
import numpy as np

capture = cv2.VideoCapture(0)
i = 0

SAMPLE_PERIOD = 10
MATCH_NUM = 6
GROUP = get_group()

def Count(capture):
    table = np.zeros(len(GROUP),dtype='i')
    for i in range(SAMPLE_PERIOD):
        ret, frame = capture.read()     # capture a on-time frame
        checked = Frame(frame)      # create a Frame class

        # keep the real time frame on the screen
        new_frame = checked.frame       # returns the frame detected
        cv2.imshow('frame', new_frame)  # show the new frame
        cv2.waitKey(1)                  # keep the frame showed

        # detect the faces in the frame
        checked.name_checked()
        name_checked = checked.names
        for name in name_checked:
            table[GROUP.index(name)] += 1

    # search for the best matched names
    checked_names = []
    for i in range(len(table)):
        if table[i] > MATCH_NUM:
            checked_names.append(GROUP[i])

    return checked_names