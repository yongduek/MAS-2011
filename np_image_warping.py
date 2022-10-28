import cv2, numpy as np 

im = cv2.imread("pixels/sogang.jpg")

# scale up
im = cv2.resize(im, (0,0), fx=2, fy=2)

Y0, X0 = np.indices(im.shape[:2], dtype=np.float32)
h, w = im.shape[:2]  # swirling center will be the image center
xc, yc = w//2, h//2
scale = 400. 
dmap = np.exp( -(np.abs(X0 - xc)/scale)**2 + -(np.abs(Y0 - yc)/scale)**2 )
# dmap /= dmap.max()
dmap = dmap * np.pi / 100
print(xc, yc, dmap.min(), dmap.max())

t = 0
while True:
    angle = dmap * t 
    X = (X0 - xc) * np.cos(angle) + (Y0 - yc) * np.sin(angle)  + xc
    Y = - (X0 - xc) * np.sin(angle) + (Y0 - yc) * np.cos(angle) + yc 
    warped = cv2.remap(im, X, Y, cv2.INTER_LINEAR)
    t += 1
    
    cv2.imshow('disp', warped)
    if cv2.waitKey(20) == 27: break
#
