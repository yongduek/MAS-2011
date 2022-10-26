import cv2, numpy as np 

def getline1(x0, y0, x1, y1):  # y = a x + b, |a} < 1
    ps = []
    dx, dy = x1 - x0, y1 - y0
    if x0 < x1:
        for x in range(x0, x1+1):
            y = dy * (x - x0) / dx + y0 
            ps.append( (x, int(y)) )
    else: # x0 > x1
        for x in range(x0, x1 - 1, -1):
            y = dy * (x - x0) / dx + y0 
            ps.append( (x, int(y)) )
    return np.array(ps)

def getline(x0, y0, x1, y1):
    dx, dy = x1 - x0, y1 - y0
    if np.abs(dy) < np.abs(dx): # slope < 1, y = ax + b
        xys = getline1(x0, y0, x1, y1)
    else: # slope >= 1, x = a y + b
        yxs = getline1(y0, x0, y1, x1)
        xys = yxs[:, ::-1]
    #
    return xys 

def getlinePQ(p, q):
    return getline(p[0], p[1], q[0], q[1])


def drawLine(canvas, p0, p1, color=(0, 128, 255)):
    xys = getlinePQ(p0, p1)
    for p in xys:
        if 0<=p[0]<canvas.shape[1] and 0<=p[1]<canvas.shape[0]:
            canvas[p[1], p[0]] = color 
    return
#

def drawPolygon(canvas, pnts, color=(0,255, 255)):
    """ pnts: Nx2 or Nx3 """
    ipnts = pnts.astype('int')
    for i in range (pnts.shape[0] - 1):
        drawLine(canvas, ipnts[i], ipnts[i+1], color)
    drawLine(canvas, ipnts[-1], ipnts[0], color)
    return 

def drawTriangle(canvas, p0, p1, p2, color=(250, 228, 250)):
    xys1 = getlinePQ(p0, p1)
    xys2 = getlinePQ(p1, p2)
    xys3 = getlinePQ(p2, p0)

    for xys in [xys1, xys2, xys3]:
        for p in xys:
            canvas[p[1], p[0]] = color 
    return 

def drawTriangleFilled_1(canvas, p0, p1, p2, color=(250, 228, 250)):
    xys1 = getlinePQ(p0, p1)
    xys2 = getlinePQ(p1, p2)
    xys3 = getlinePQ(p2, p0)

    xys = np.vstack( (xys1, xys2, xys3) )
    # print(xys1.shape, xys2.shape, xys3.shape, xys.shape)
    # print(xys)
    
    # sort by column 0 (x coord), if x values are same, then sort by y, i.e., column 1
    xys = xys[xys[:,0].argsort()]  # sort by x coord
    xys = xys[xys[:,1].argsort(kind='stable')] # sort by y coord, but x 좌표의 순서는 바뀌지 않음
    # print(xys)
    
    k = 0
    while k < xys.shape[0]:
        x = xys[k, 0]
        y = xys[k, 1]
        i = k + 1
        while (i < xys.shape[0]):
            if y == xys[i, 1]:  # y 좌표가 같은 점들을 고르고
                i += 1
            else:
                break # 다르면 중지.
        # 이제 xys[i-1,1] 이 마지막으로 동일한 y 좌표값.
        # print(f"start: {xys[k]}  end: {xys[i-1]}")
        xstart = xys[k, 0]
        xend = xys[i-1, 0]
        for xm in range(xstart, xend+1):
            canvas[y, xm] = color

        k = i 
    #
    
    return # finished.


def drawTriangleFilled(canvas, q0, q1, q2, color=(250, 228, 250)):
    p0 = q0.astype(int)
    p1 = q1.astype(int)
    p2 = q2.astype(int)
    
    xys1 = getlinePQ(p0, p1)
    xys2 = getlinePQ(p1, p2)
    xys3 = getlinePQ(p2, p0)

    xys = np.vstack( (xys1, xys2, xys3) )
    # print(xys1.shape, xys2.shape, xys3.shape, xys.shape)
    # print(xys)
    
    # sort by column 0, if x values are same, then sort by y, i.e., column 1
    ymin = xys[:,1].min()
    ymax = xys[:,1].max()
    #
    for y in range(ymin, ymax+1):
        # 1. find x values, for the same y
        xcoords = []
        for xy in xys:
            if xy[1] == y:
                xcoords.append(xy[0]) # collect x only
        #
        xmin, xmax = min(xcoords), max(xcoords)
        canvas[y, xmin:xmax+1] = color 
    #    
    return # finished.   
#

def Rotation(deg):
    R = np.eye(3)
    radian = np.deg2rad(deg)
    c, s = np.cos(radian), np.sin(radian)
    R[0,0] = c
    R[0,1] = -s
    R[1,0] = s
    R[1,1] = c
    return R 

def Translation(t): # t is a 2/3-vector
    T = np.eye(3)
    T[0,2] = t[0]
    T[1,2] = t[1]
    return T

def Scaling(s):
    S = np.eye(3)
    S[0,0] = S[1,1] = s 
    return S 

def Shear(h):
    H = np.eye(3)
    H[0,1] = h 
    return H 
#

if __name__ == "__main__":
    width, height = 1800, 1400
    canvas = np.zeros((height, width, 3), dtype='uint8')
 
    Wing = np.array([[0, -50, 1], [200, 0, 1], [0, 50, 1]]).T 
    w, h = 150, 450
    
    Pillar  = np.array([[0,0,1], [w, 0, 1], [w, h, 1], [0,h,1]]).T
    x0, y0 = 900, 800
    
    degree = 30
    
    while True:
        canvas.fill(0)
        # draw a random triangle
        # xy3 = np.random.randint([0, 0], [width, height], size=(3, 2))
        # color = np.random.randint(0, 256, size=3)
        # # drawTriangle(canvas, xy3[0], xy3[1], xy3[2], color)
        # drawTriangleFilled(canvas, xy3[0], xy3[1], xy3[2], color)

        # Pillar 
        Hpillar = Translation([x0, y0])
        Qpillar = Hpillar @ Pillar
        drawPolygon(canvas, Qpillar.T)

        # Wing 1
        for shift in [0, 90, 180, 270]:
            H1 = np.eye(3) @ Hpillar @ Translation([w/2, 0]) @ Rotation(degree + shift) @ Translation([-200, 0]) 
            Wing1 = H1 @ Wing 
            drawPolygon(canvas, Wing1.T, color=(255, 255, 0))
            drawTriangleFilled(canvas, Wing1[:,0], Wing1[:,1], Wing1[:,2], (255, 125, 55))
                            
        cv2.imshow("Canvas", canvas)
        ch = cv2.waitKey(30)
        if ch == 27: break 
        
        degree += 15
    #
    
    cv2.imwrite("canvas.png", canvas)
#