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

    columns = np.zeros((height, nframes, 3), dtype='uint8')
    i = 0
    while video.isOpened():
        ret, frame = video.read() 
        if ret == False:
            break

        array = frame # just rename, nothing

        # Collapse down to a column.
        # column = array.mean(axis=1)  # (height, 3)
        # Convert to bytes, as the `mean` turned our array into floats.
        # column = column.clip(0, 255).astype('uint8')

        column = array[:, array.shape[1]//2]

        if i < 3: 
            print(i, frame.shape, type(frame), column.shape)

        columns[:,i,:] = column

        i += 1

        cv2.imshow('frameWindow', array)
        if cv2.waitKey(1) == 27:  # ESC
            break
    #
    print(f'finished processing {i} frames ({nframes})')

    full_array = columns 
    print(len(columns), full_array.shape)

    full_array = cv2.resize(full_array, (800,200)) # make a smaller version
    print(full_array.dtype)

    imageio.imwrite('barcode_cv2_numpy.jpg', full_array)

    cv2.imshow('frameWindow', full_array)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()