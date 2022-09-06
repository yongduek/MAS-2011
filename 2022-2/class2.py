# pip install opencv-python

import cv2 

im = cv2.imread("busan.jpg")  #

im[100, 200, 0] = 0
im[100, 200, 1] = 0
im[100, 200, 2] = 255

while True:
    cv2.imshow("display", im)

    ch = cv2.waitKey(30)
    if ch == 27:
        break 
#