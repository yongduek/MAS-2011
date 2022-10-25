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

    canvas = np.zeros((height, nframes//3, 3), dtype='uint8')
    i = 0
    while video.isOpened():
        ret, frame = video.read() 
        if ret == False:
            break
        array = frame # just rename, nothing
        rows, cols = frame.shape[:2]
        
        # 1. block shift to the left
        # canvas[:,:-1,:] = canvas[:,1:,:]
        for r in range(canvas.shape[0]):  # every r-elem
            for c in range(canvas.shape[1] - 1):
                for k in range(3):
                    canvas[r,c,k] = canvas[r, c+1, k]
        
        # 2. put the new column at the last of the column
        # canvas[:,-1,:] = array[:, array.shape[1]//2, :]
        cmid = array.shape[1] // 2  # middle location
        for r in range(rows):
            for k in range(3):
                canvas[r, canvas.shape[1] - 1, k] = array[r, cmid, k]

        cv2.imshow('frameWindow', array)
        cv2.imshow('canvas', canvas)
        
        if cv2.waitKey(1) == 27:  # ESC
            break
    #
    print(f'finished processing {i} frames ({nframes})')

    cv2.waitKey(0)

if __name__ == "__main__":
    main()