# draw random lines using opencv display/rendering function
#
import cv2
import numpy as np 
import random # generic python package

rng = np.random.default_rng(2021)

im = np.zeros(shape=(1024, 1800, 3), dtype='uint8')
rows, cols, depth = im.shape 

while cv2.waitKey(10) != 27:

    pts = []
    for _ in range(2):
        # numpy ints are not accepted to some of opencv functions (e.g. color)
        # in simple cases, just use python's generic random library
        #
        # y = rng.integers(low=0, high=rows+1)
        # x = rng.integers(low=0, high=cols+1)
        y = random.randint(0, rows)
        x = random.randint(0, cols)
        pts.append((x, y))
        # print(type(x))
    #
    thickness = np.random.randint(low=1, high=100)
    #
    # np.tolist() is a way
    color = rng.integers(low=0, high=256, size=3, dtype='int32').tolist()
    # or use generic random
    # color = [random.randint(0, 255) for _ in range(3)]

    # print('color: ', color, type(color), type(color[0]))

    cv2.line(im, pts[0], pts[1], color, thickness=thickness)

    cv2.imshow('window', im)
#