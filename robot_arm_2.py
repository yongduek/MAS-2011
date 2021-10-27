# 서용덕 101
# draw an arm with Translation + rotation

import sys 
import cv2 # opencv-python
import numpy as np 
import matplotlib.pyplot as plt 

print('python version: ', sys.version)
print('opencv version: ', cv2.__version__)
print('numpy version: ', np.__version__)

print(__file__) 

# display canvas
im = np.zeros((1000, 1800, 3), dtype=np.uint8)
rows, cols, depth = im.shape 
width, height = cols, rows

rng = np.random.default_rng(908)

def drawLine(im, pt1, pt2, color):
    cv2.line(im, pt1, pt2, color)

def drawPolygon(im, ptlist, color):
    # ptlist = [pt0, pt1, pt2, ..., pt_{n-1}], n points 
    n = len(ptlist)
    for i in range(1, n):
        drawLine(im, ptlist[i], ptlist[i-1], color)
    drawLine(im, ptlist[n-1], ptlist[0], color)
#

def getRect(w=4, h=2):
    hw = w / 2
    hh = h / 2 
    vertices = [ [hw, hh], [-hw, hh], [-hw, -hh], [hw, -hh]]
    vertices = np.array(vertices)
    return vertices
#

def Translate(tx, ty):
    m = np.eye(3)
    m[0,2] = tx 
    m[1,2] = ty
    return m 
#

def Rotate(deg):
    m = np.eye(3)
    rad = deg * (np.pi * 2 / 360.)
    c = np.cos(rad)
    s = np.sin(rad)
    m[0,0] = c 
    m[0,1] = -s 
    m[1,0] = s 
    m[1,1] = c 
    return m 

def transform(M, varr):
    """
    M: 3x3
    varr: Nx2

    res = M[:2,:2] @ varr.T + M[:,2]
    res = M @ np.hstack((varr, ones))
    """
    ones = np.ones((varr.shape[0], 1))
    varr_homo = np.hstack((varr, ones)) # Nx3
    varr_homo = varr_homo.T # transpose, 3xN
    res = np.matmul(M, varr_homo) # 3xN
    res = res.T # Nx3
    res = res[:,:2] # Nx2
    # print(varr)
    # print(ones)
    # print(varr_homo)
    # print(res)
    return res 

def main():
    print('main loop')

    arm = getRect(200, 100);

    done = False 

    angle = 30. # degree 

    while done == False:
        # keyboard input
        ch = cv2.waitKey(10)
        if ch == 27: 
            done = True 

        # -- update ------------
        angle += 1.

        # -- clear canvas ------
        im[:,:,:] = 0 

        # ----------------------
        T0 = Translate(300, 200)
        T1 = Rotate(angle)
        TransRot = T1 @ T0   # matrix multiplication for two numpy matrices
        V = transform(TransRot, arm)
        V = V.astype('int')
        color = (255, 255, 0)
        drawPolygon(im, V, color)

        RotTrans = T0 @ T1
        V = transform(RotTrans, arm)
        V = V.astype('int')
        color = (0, 255, 255)
        drawPolygon(im, V, color)


        # display canvas
        cv2.imshow('my canvas', im)

    # while

    pass 


# interface with cmd or OS
if __name__ == "__main__":
    main()
