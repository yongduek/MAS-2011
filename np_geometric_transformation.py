import numpy as np 
import cv2 

def isTriangle(pts):
    # your code here
    return True

def getline(x0, y0, x1, y1):
    pass 

def drawLine(cvs, x0, y0, x1, y1, color):
    shape = cvs.shape
    if 0: # you should make this
        xys = getline(x0, y0, x1, y1)
        for xy in xys:
            if (0 <= xy[0] < shape[1]) and (0 <= xy[1] < shape[0]):
                cvs[xy[1], xy[0]] = color
    else:
        cv2.line(cvs, (x0, y0), (x1, y1), tuple([int(c) for c in color]))
    return 

def drawLinePQ(cvs, p, q, color):
    drawLine(cvs, p[0], p[1], q[0], q[1], color)

def drawPolygon(cvs, pts, color, axis=False):
    for k in range(pts.shape[0] - 1):
        drawLinePQ(cvs, pts[k], pts[k+1], color)
    drawLinePQ(cvs, pts[-1], pts[0], color)
    
    if axis == True:
        center = (pts.sum(axis=0) / pts.shape[0]).astype(int) # average point
        drawLinePQ(cvs, center, pts[0], color=(0, 255, 255))

def deg2rad(deg):
    return deg * np.pi / 180.

def getRegularPolygon(n):
    pts = []
    delta = 360. / n 
    for i in range(n):
        deg = delta * i 
        radian = deg2rad(deg)
        x = np.cos(radian)
        y = np.sin(radian)
        pts.append((x, y))
    #
    return np.array(pts)
#

def getRotation(deg):
    R = np.zeros((2,2))
    radian = deg2rad(deg)
    R[0,0] = np.cos(radian)
    R[0,1] = -np.sin(radian)
    R[1,0] = np.sin(radian)
    R[1,1] = np.cos(radian)
    return R 

def main(argv):
    cwidth, cheight = 1600, 1000 
    color_depth = 3
    canvas = np.zeros( (cheight, cwidth, color_depth), dtype='uint8')


    color = np.random.randint(0, 256, size=3)
    ngon = 5
    points0 = getRegularPolygon(ngon)
    scale = 300
    shift = [cwidth/2, cheight/2]
    degree = 0  # initial rotation angle
    
    #display loop 
    while True:
        canvas[:,:,:] = 0 # clear the canvas
        
        # 1. generate a random line and draw
        if 0:
            x0 = np.random.randint(0, cwidth)
            y0 = np.random.randint(0, cheight)
            x1 = np.random.randint(0, cwidth)
            y1 = np.random.randint(0, cheight)
            color = np.random.randint(0, 256, size=3)
            drawLine(canvas, x0, y0, x1, y1, color)
        #
                
        # 2. draw a random Triangle
        if 0:
            color = np.random.randint(0, 256, size=3)
            points = np.random.randint([0, 0], [cwidth, cheight], size=(3,2))
            if isTriangle(points) == True:
                drawPolygon(canvas, points, color)
        
        # 3. draw a regular polygon
        if 0:
            color = np.random.randint(0, 256, size=3)
            ngon = np.random.randint(4, 10) # ngon 
            points = getRegularPolygon(ngon)
            scale_random = np.random.uniform(100, 400)
            shift_x = np.random.randint(0, cwidth)
            shift_y = np.random.randint(0, cheight)
            points = points * scale_random 
            points = points + [shift_x, shift_y]

            points = points.astype('int')
            drawPolygon(canvas, points, color)

        # 4. draw a regular polygon with Rotation & Translation        
        if 0:
            color = np.random.randint(0, 256, size=3)
            ngon = np.random.randint(4, 10) # ngon 
            points = getRegularPolygon(ngon)
            scale_random = np.random.uniform(100, 400)
            R = getRotation(np.random.randint(0, 360))
            # R = getRotation(30)
            points = points @ R.T # rotate the points
            shift_x = np.random.randint(0, cwidth)
            shift_y = np.random.randint(0, cheight)
            points = points * scale_random 
            points = points + [shift_x, shift_y]
            
            points = points.astype('int')
            drawPolygon(canvas, points, color)
        #
        
        # print(f"degree: {degree}")
        R = getRotation(degree)
        points = points0 @ R.T # rotate the points
        points = points * scale + shift 
        points = points.astype('int')
        drawPolygon(canvas, points, color, axis=True)

        degree += 1
        # display
        cv2.imshow("window name", canvas)
        if cv2.waitKey(20) == 27: break 
        
    #
    pass 
#

if __name__ == "__main__":
    import sys 
    main(sys.argv)