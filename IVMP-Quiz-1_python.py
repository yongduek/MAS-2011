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


GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
RED = (0, 0, 255)

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2


# display canvas
im = np.zeros((1000, 1800, 3), dtype=np.uint8)
rows, cols, depth = im.shape 
width, height = cols, rows

rng = np.random.default_rng(908)

def drawLine(im, pt1, pt2, color):
    cv2.line(im, pt1, pt2, color, thickness=3)

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

def draw(TA, arm, string="", color=None):
    V = transform(TA, arm)
    print(string, np.dot(TA, [0,0,1]))
    V = V.astype('int')
    if color is None:
        color = [255, 255, 255]
    drawPolygon(im, V, color)
    return np.mean(V, axis=0).astype('int')
#

def drawAxis(x, y):
    drawLine(im, [x, y], [x+400, y], [0, 0, 120])
    drawLine(im, [x, y], [x, y+300], [0, 140, 0])

def main():
    print('main loop')

    arm = getRect(200, 100);
    star = getRect(100, 50);

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
        # Q1        
        TA1 = Translate(400,300) @ Rotate(35)
        x = draw(TA1, arm, "Q1", GREEN)
        cv2.putText(im,'Q1', x, font, fontScale, GREEN, lineType)

        # Q2
        TA2 = Rotate(50) @ Translate(100,0) #@ Rotate(50)
        v2 = draw(TA2, arm, "Q2", BLUE)
        cv2.putText(im,'Q2', v2, font, fontScale, BLUE, lineType)

        TA22 = Translate(100,0) @ Rotate(50)  # Wrong solution
        v22 = draw(TA22, arm, "Q22", RED)
        cv2.putText(im,'Q2 Wrong', [v22[0], v22[1]], font, fontScale, RED, lineType)

        # Q3
        BaseT = Translate(800, 200)
        drawAxis(800, 200)
        # drawLine(im, [800, 200], [1500, 200], [0, 0, 120])
        # drawLine(im, [800, 200], [800, 500], [0, 140, 0])
        alpha = 40
        beta = -13 - angle/90.
        TA3 = BaseT @ Rotate(alpha) @ Translate(100,0)
        x = draw(TA3, arm, "Q3A", [255, 255, 0])
        cv2.putText(im,'A3', x, font, fontScale, [255, 255, 0], lineType)

        TB3 = TA3 @ Translate(100, 0) @ Rotate(beta) @ Translate(100, 0)
        x = draw(TB3, arm, "Q3B", [255, 255, 140])
        cv2.putText(im,'B3', x, font, fontScale, [255, 255, 140], lineType)


        # Q4
        BaseT = Translate(-400, -100)
        cv2.putText(im,'Q4', [-400+900, -100+800], font, fontScale, fontColor, lineType)
        # drawAxis(200, 400)
        beta4 = -33 - angle*2
        d4 = 400 # instead of 11 
        TA4 = BaseT @ Translate(900, 800) @ Rotate(90)
        draw(TA4, arm, "Q4A", [0, 255, 255])
        TB4 = TA4 @ Rotate(-90) @ Rotate(beta4) @ Translate(d4, 0) @ Rotate(-beta4)
        x = draw(TB4, star, "Q4B", [0, 140, 140])
        cv2.putText(im,'B4star?', x, font, fontScale, [255, 140, 140], lineType)

        # Q5
        BaseT = Translate(200, -100)
        cv2.putText(im,'Q5', [200+900, -100+800], font, fontScale, fontColor, lineType)
        # drawAxis(200, 400)
        beta5 = -33 - angle/100.
        d5 = 400 # instead of 11 
        TA5 = BaseT @ Translate(900, 800) @ Rotate(90)
        draw(TA5, arm, "Q5A", [255, 140, 255])

        TB5 = TA5 @ Rotate(-90) @ Rotate(beta5) @ Translate(d5, 0) @ Rotate(-beta5)
        x = draw(TB5, star, "Q5B", [255, 140, 140])
        cv2.putText(im,'star?', x, font, fontScale, [255, 140, 140], lineType)

        gamma5 = -80 - 8*angle/10.
        dB5 = 50*3  # instead of 5
        TX = TB5 @ Rotate(gamma5) @ Translate(dB5, 0) @ Rotate(-gamma5)
        arm2 = getRect(40, 20);
        color = [100, 100, 255]
        x = draw(TX, arm2, "Q4X", )
        cv2.putText(im,'X', x, font, fontScale, color, lineType)


        # display canvas
        cv2.imshow('my canvas', im)

    # while

    pass 


# interface with cmd or OS
if __name__ == "__main__":
    main()
