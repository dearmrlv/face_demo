from frame import Frame
import cv2
from imtools import get_group
import numpy as np

capture = cv2.VideoCapture(0)
i = 0

SAMPLE_PERIOD = 10
MATCH_NUM = 2
GROUP = get_group()

def Count(capture):
    table = np.zeros(len(GROUP),dtype='i')
    for i in range(SAMPLE_PERIOD):
        ret, frame = capture.read()     # capture a on-time frame
        checked = Frame(frame)      # create a Frame class
        # keep the real time frame on the screen
        # detect the faces in the frame
        checked.name_checked()
        # to transform the frame failed to detect
        # checked.re_detect(2)
        new_frame = checked.frame  # returns the frame detected
        cv2.imshow('frame', new_frame)  # show the new frame
        cv2.waitKey(1)  # keep the frame showed
        name_checked = checked.names
        # counting faces
        for name in name_checked:
            try:
                table[GROUP.index(name)] += 1
            except: ValueError

    # search for the best matched names
    checked_names = []
    for i in range(len(table)):
        if table[i] > MATCH_NUM:
            checked_names.append(GROUP[i])

    return checked_names


def main():
    flag = 1
    while(True):
        # ret, frame = capture.read()
        # checked = Frame(frame)
        # checked.name_checked()
        # new_frame = checked.frame
        # cv2.imshow('frame', new_frame)
        # cv2.waitKey(1)
        checked_names = Count(capture)
        if len(checked_names) != 0:
            flag = 1
            print('<---Names--->')
            print(checked_names)
        else:
            if flag == 1:   # flag is for decrease the same output
                print('Face Recognition Failed. Please choose a brighter environment for detection')
                flag = 0


if __name__ == '__main__':
    main()