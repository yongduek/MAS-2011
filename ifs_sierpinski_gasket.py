import os, sys 
import numpy as np 
import cv2 

def midpoint(a, b):
    return (a + b)/2.

def Sierpinski(T3, im, bgr, npoints=1000):
    ip = np.random.randint(len(T3))
    p = T3[ip]
    while True:
    # for k in range(npoints):
        iT = np.random.randint(len(T3))
        p = midpoint(T3[iT], p)
        x, y = int(p[0]), int(p[1])
        im[y, x] = bgr
        # cv2.drawMarker(im, (x, y), bgr)
        cv2.imshow("dispWindow", im)
        ch = cv2.waitKey(1)
        if ch == 27: break 
    return
#

if __name__ == "__main__":
    im = np.zeros((1000, 1080, 3), dtype=np.uint8)
    
    ys = np.random.randint(0, im.shape[0], size=3)
    xs = np.random.randint(0, im.shape[1], size=3)
    bgr = tuple(map(int, np.random.randint(100, 255, size=3) ))

    T3list = [np.array([x, y]) for x, y in zip(xs, ys)]
    Sierpinski(T3list, im, bgr)  
    