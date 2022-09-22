import cv2, numpy as np 

def deg2rad(deg):
    return deg * np.pi / 180

im = cv2.imread("pixels/image-15.png")
canvas = np.zeros((1200, 2000, 3), dtype='uint8')

th = 0 #deg2rad(30)

while True:
    
    th += 2
    radian = deg2rad(th)
    
    # simple forward mapping
    for y in range(im.shape[0]):
        for x in range(im.shape[1]):
            xc = x * np.cos(radian) - y * np.sin(radian)
            yc = x * np.sin(radian) + y * np.cos(radian)
            
            xc, yc = int(xc), int(yc) 
            
            if 0 <= xc < canvas.shape[1] and 0 <= yc < canvas.shape[0]:
                canvas[yc, xc] = im[y, x]
    #

    cv2.imshow("canvas", canvas)
    ch = cv2.waitKey(10)
    if ch == 27: break 
#