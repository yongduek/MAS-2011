# 서용덕 101

import sys 
import cv2 # opencv-python
import numpy as np 
import matplotlib.pyplot as plt 

print('python version: ', sys.version)
print('opencv version: ', cv2.__version__)
print('numpy version: ', np.__version__)

print(__file__) 

# filename = 'RickMorty-bg.jpg'
# im = cv2.imread(filename)
im = np.zeros((800, 1000, 3), dtype=np.uint8)
rows, cols, depth = im.shape 
width, height = cols, rows

print(type(im), im.shape)

# plt.imshow(im)
# plt.show()

rng = np.random.default_rng(908)

n = rng.integers(0, 10)
print(n, type(n))

def drawLine(im, pt1, pt2, color):
    cv2.line(im, pt1, pt2, color)

def drawLineDIY(im, pt1, pt2, color):
    # y = (x - x0) * (y1 - y0) / (x1 - x0) + y0
    x0, y0 = pt1 
    x1, y1 = pt2 

    # print('-------')
    # m = (y1 - y0) / (x1 - x0) # error when x1 == x0

    # condition = np.abs(m) < 1  # abs( (y1-y0) / (x1-x0) ) < 1
    condition = abs(y1-y0) < abs(x1-x0)
    
    if condition:
        # if x0 > x1 ?
        if x0 > x1:
            # swap
            # t = x0 
            # x0 = x1 
            # x1 = t 
            # print("x0 > x1", x0, x1)
            pass 

        m = (y1 - y0) / (x1 - x0)
        for x in range(x0, x1+1, 1):
            y = (x - x0) * m + y0
            y = int(y + .5)
            im[y, x, :] = color
    else:
        if y0 > y1:
            #
            pass 

        m = (x1 - x0) / (y1 - y0)
        for y in range(y0, y1+1, 1):
            x = (y - y0) * m + x0 
            x = int(x + .5)
            im[y, x, :] = color
    pass

def drawTriangle(im, p1, p2, p3, color):
    drawLine(im, p1, p2, color)
    drawLine(im, p2, p3, color)
    drawLine(im, p3, p1, color)
#

def drawPolygon(im, ptlist, color):
    # ptlist = [pt0, pt1, pt2, ..., pt_{n-1}], n points 
    n = len(ptlist)
    for i in range(1, n):
        drawLine(im, ptlist[i], ptlist[i-1], color)
    drawLine(im, ptlist[n-1], ptlist[0], color)
#

def getRandomPoint():
    return (rng.integers(width), rng.integers(height)) 

def getRegularPolygon(n, cxy=(250, 250), radius=100):
    #
    ptlist = []
    delta_angle = 360./ n 
    for i in range(n):
        angle = 2*np.pi * delta_angle * i / 360.
        pt = int(radius*np.cos(angle)) + cxy[0], int(radius * np.sin(angle)) + cxy[1] # radian or degree ?
        ptlist.append( pt )
    return ptlist

def drawStellation(im, ptlist, color): 
    """ connect every other vertex """
    n = len(ptlist)
    for i in range(n):
        drawLine(im, ptlist[i], ptlist[(i+2)%n], color)
    return 

def drawRosette(im, ptlist, color):
    """ connect each vertex to every other vertex """
    n = len(ptlist)
    for i in range(n-1):
        for j in range(i+1, n):
            drawLine(im, ptlist[i], ptlist[j], color)
    return 
#

def getCardioid(K=100, cxy=(300, 300)):
    """ r = K(1+cos\th)
    """
    def rfunc(th):
        return K * (1 + np.cos(th))

    ptlist = []
    n = 50
    delta_angle = 360./ n 
    for i in range(n):
        angle = 2*np.pi * delta_angle * i / 360.
        r = rfunc(angle)
        x = int(r * np.cos(angle))
        y = int(r * np.sin(angle))

        pt = (x + cxy[0], y+cxy[0]) # radian or degree ?
        ptlist.append( pt )

    return ptlist

def getRoseInt(K=100, n=3, cxy=(300, 300)):
    """ r = cos(n\th)
    """
    def rfunc(th):
        return K * (np.cos(n * th))

    ptlist = []
    ngrids = 150
    delta_angle = 360./ ngrids 
    for i in range(ngrids):
        angle = 2*np.pi * delta_angle * i / 360.
        r = rfunc(angle)
        x = int(r * np.cos(angle))
        y = int(r * np.sin(angle))

        pt = (x + cxy[0], y+cxy[1]) # radian or degree ?
        ptlist.append( pt )

    return ptlist

def getRose(K=100, n=3):
    """ r = cos(n\th)
    """
    def rfunc(th):
        return K * np.cos(n * th)

    ptlist = []
    ngrids = 150
    delta_angle = 360./ ngrids 
    for i in range(ngrids):
        radian = delta_angle * i * (2 * np.pi / 360.)  # deg -> rad
        r = rfunc(radian)
        x = r * np.cos(radian)
        y = r * np.sin(radian)

        pt = (x, y) # radian or degree ?
        ptlist.append( pt )

    return np.array(ptlist)
#

def getRotation(degree):
    rad = np.deg2rad(degree)
    c = np.cos(rad) 
    s = np.sin(rad) 
    R = np.array([[c, -s], [s, c]])
    return R 

rot_angle = 45

while cv2.waitKey(1000) != 27: 
    pt1 = (rng.integers(width), rng.integers(height))
    # pt2 = (700, 400)
    pt2 = (rng.integers(width), rng.integers(height))
    pt3 = (rng.integers(width), rng.integers(height))

    color = (int(rng.integers(256)), int(rng.integers(256)), int(rng.integers(256)))
    
    # drawLine(im, pt1, pt2, color)

    # drawTriangle(im, pt1, pt2, pt3, color)

    # a polygon (4, 5, 10)
    # ptlist = [getRandomPoint() for _ in range(5)]
    # drawPolygon(im, ptlist, color) 
    
    k = rng.integers(5, 16)
    
    cx = rng.integers(width)
    cy = rng.integers(height)
    # ptlist = getRegularPolygon(k, cxy=(cx, cy), radius=200)
    # drawPolygon(im, ptlist, color)

    # drawStellation(im, ptlist, color)
    # drawRosette(im, ptlist, color)
    # ptlist = getCardioid(K=100, cxy=(cx, cy))
    # drawPolygon(im, ptlist, color)

    Vrose = getRose(K=200, n=rng.integers(3, 7))

    # Vrose += np.array([300, 150])  # translate
    ptlist = Vrose.astype('int')   # discretize
    drawPolygon(im, ptlist, color)

    # Rmat = getRotation(rot_angle)

    # rot_angle += 10

    cv2.imshow('mywindow', im) 
#
cv2.imwrite('redcolor.png', im)
#
#
import os 

dirname = os.path.dirname(__file__)
print(dirname)
print(__file__)