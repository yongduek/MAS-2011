           
import os, sys 
import numpy as np 
import cv2 

def Clifford(x, y, a, b, c, d, *o):
    return np.sin(a * y) + c * np.cos(a * x), \
           np.sin(b * x) + d * np.cos(b * y)


if __name__ == "__main__":
    im = np.zeros((1000, 1080, 3), dtype=np.uint8)   
    bgr = tuple(map(int, np.random.randint(100, 255, size=3) ))

    # init & parameters               
    x, y, a, b, c, d = 0, 0, -1.3, -1.3, -1.8, -1.9
    scale = 200.
    shift = 500

    while True:
        for _ in range(100):  # at once
            x, y = Clifford(x, y, a, b, c, d)
            
            xx = int(x * scale + shift)
            yy = int(y * scale + shift)
            
            if xx >= 0 and xx < im.shape[1] and yy >= 0 and yy < im.shape[0]:
                im[yy, xx] = bgr
            
        cv2.imshow("dispWin", im)
        
        ch = cv2.waitKey(1)
        if ch == 27: break 