"""
https://smirnov-am.github.io/chromakeying/
Chroma keying - or blue/green screen matting - is a process of removing a specific color from the video to be replaced with another picture or video. Historically green or blue colors were used as a background because they are not dominant in human skin or clothes. However, when a weather forecaster puts on a green skirt it can lead to funny situations:
"""

import cv2
import imageio 

# https://docs.opencv.org/4.5.1/dd/d43/tutorial_py_video_display.html

import numpy as np
import imageio
import os 
from pathlib import Path
import cv2 # opencv 

def chromaKeyGreen(array, keyvalue):
    for r in range(array.shape[0]):
        for c in range(array.shape[1]):
            if array[r,c,1] == keyvalue:
                array[r,c] = 0
    return array
#


def main():
    cwd = os.path.dirname(__file__)
    print('cwd: ', cwd)

    # size reduced:
    # ffmpeg -i squid.mp4 -vf scale=720:400 squid_720x480.mp4

    filename = Path(cwd) / 'pixels/squid_720x480.mp4'
    print(filename)

    # open the video file
    video = cv2.VideoCapture(str(filename))

    # retrieve movie information
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)  # this may be float such as 29.97
    nframes = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fourcc = int(video.get(cv2.CAP_PROP_FOURCC))

    print(width, height, fps, nframes, fourcc)

    i = 0
    while video.isOpened():
        ret, frame = video.read()
        cv2.imwrite('squid_720x480_frame_0.png', frame)
        break
        if not ret:
            # frame read error
            # do something
            break

        # chroma key based on the green color intensity
        array = chromaKeyGreen(frame, 255)

        cv2.imshow('frameWindow', array)
        if cv2.waitKey(1) == 27:  # ESC
            break
    #
    print(f'finished processing {i} frames ({nframes})')
#

# start
main()
