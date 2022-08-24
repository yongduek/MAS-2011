import os, sys 
import numpy as np 
import cv2 

if __name__ == "__main__":
    im = np.zeros((1024, 1280, 3), dtype=np.uint8)
    
    while True:
        ys = np.random.randint(0, im.shape[0], size=2)
        xs = np.random.randint(0, im.shape[1], size=2)
#        bgr = tuple(int(a) for a in np.random.randint(0, 255, size=3))
        bgr = tuple(map(int, np.random.randint(0, 255, size=3) ))
        
        cv2.line(im, (xs[0], ys[0]), (xs[1], ys[1]), bgr)
        
        cv2.imshow("dispWindow", im)
        
        ch = cv2.waitKey(10)  # press ESC to stop
        if ch == 27: break