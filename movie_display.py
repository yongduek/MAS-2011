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
    spf = int(1000. / fps )
    
    print(width, height, fps, nframes, fourcc, spf)

    while video.isOpened():
        ret, frame = video.read() 
        if ret == False:
            break
        
        cv2.imshow('frameWindow', frame)
        if cv2.waitKey(10) == 27:  # ESC
            break
    #

if __name__ == "__main__":
    main()