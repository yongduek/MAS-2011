import numpy as np
import cv2 # opencv

rows = 768
cols = 1024
im = 255 * np.ones((rows, cols, 3), dtype='uint8')

def drawPixel(im, r, c, color=(0, 0, 255)):  # BGR, don't forget
    im[r,c] = color
    return 

def drawLine(im, r0, c0, r1, c1, color=(0,0,0)):
    for c in range(c0, c1+1):
        r = int((c-c0) * (r1 - r0) / (c1 - c0) + r0 )
        drawPixel(im, r, c, color)
        # im[r,c] = color 
    return 

while True:

    # draw
    r = np.random.randint(rows)
    c = np.random.randint(cols)

    drawPixel(im, r, c)

    drawLine(im, 100, 100, 200, 400)

    pt1 = (100, 110)
    pt2 = (400, 210)
    color=(255, 0, 0)

    cv2.line(im, pt1, pt2, color)
    # display
    cv2.imshow('win', im)

    # ESC?
    if cv2.waitKey(1) == 27: break