# pip install opencv-python

import numpy as np 
import cv2  # opencv


if __name__ == "__main__":
    print("This is main!")
    
    ncols = 1024
    nrows = 760
    width, height = ncols, nrows
    im = np.zeros(nrows * ncols * 3, dtype=np.uint8)   # image memory allocation
        
    # blue line at x: 200, 200+400, y=100
    y0 = 100
    for x in range(200, 200 + 400):
        i = y0 * width * 3 + x * 3
        im[i] = 0
        im[i + 1] = 0
        im[i + 2] = 255
        
    # blue rectangle at: x0=200, y0=100, width=400, height = 300
    x0, y0 = 200, 150
    bwidth, bheight = 400, 300
    for x in range(x0, x0 + bwidth):
        for y in range(y0, y0 + bheight):
            indx = width * 3 * y + x * 3
            im[indx + 0] = 255
            im[indx + 1] = 0
            im[indx + 2] = 0
            
    im = im.reshape(nrows, ncols, 3)
    cv2.imshow("window", im)  # opencv thinks it is in BGR order
    
    ch = cv2.waitKey()
    
    # save to a file
    cv2.imwrite("im_created.png", im)