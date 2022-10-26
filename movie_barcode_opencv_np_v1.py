# https://docs.opencv.org/4.5.1/dd/d43/tutorial_py_video_display.html

import numpy as np
import imageio
import os 
from pathlib import Path
import cv2 # opencv 

def main():
    cwd = os.path.dirname(__file__)
    print('cwd: ', cwd)

    filename = Path(cwd) / 'pixels/time-lapse-video-of-sunset-by-the-sea-854400.mp4'
    print(filename)

    video = cv2.VideoCapture(str(filename))

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)  # this may be float such as 29.97
    nframes = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fourcc = int(video.get(cv2.CAP_PROP_FOURCC))

    print(width, height, fps, nframes, fourcc)

    columns = np.zeros((height, nframes//3, 3), dtype='uint8')
    i = 0
    while video.isOpened():
        ret, frame = video.read() 
        if ret == False:
            break
        array = frame # just rename, nothing

        # 1. block shift to the left
        columns[:,:-1,:] = columns[:,1:,:]
        
        # 2. put the new column at the last of the column
        columns[:,-1,:] = array[:, array.shape[1]//2, :]

        cv2.imshow('frameWindow', array)
        cv2.imshow('columns', columns)
        
        if cv2.waitKey(1) == 27:  # ESC
            break
    #
    print(f'finished processing {i} frames ({nframes})')

    cv2.waitKey(0)

if __name__ == "__main__":
    main()