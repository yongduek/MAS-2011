import cv2, numpy as np 

def deg2rad(deg):
    return deg * np.pi / 180

def main():
    im = cv2.imread("pixels/image-15.png")
    canvas = np.zeros((1200, 2000, 3), dtype='uint8')

    th = 0 #deg2rad(30)

    while True:
        canvas[:,:,:] = 0 # clear the canvas
                
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

        # backward mapping
        for y in range(canvas.shape[0]):
            for x in range(canvas.shape[1]):
                c, s = np.cos(radian), np.sin(radian)
                u = x * c + y * s 
                v = -x * s + y * c 
                ui, vi = int(u), int(v) 
                if 0 <= ui < im.shape[1] - 1 and 0 <= vi < im.shape[0] - 1:
                    bgr = im[vi, ui].astype('int') + im[vi+1, ui] + im[vi+1, ui+1] + im[vi, ui+1]
                    bgr = bgr / 4
                    bgr = bgr.astype('uint8')  # use clip() !
                    canvas[y, x] = bgr 

        #
        cv2.imshow("canvas", canvas)
        ch = cv2.waitKey(10)
        if ch == 27: break 
    #


if __name__ == "__main__":
    main()